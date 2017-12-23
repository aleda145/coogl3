"""
Search module for the Twitter API
"""

import os
import re
import time
import datetime
import pickle
import glob

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
# TODO add access tokens here!
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

# Variables for tracked keywords in search,
# time until the stream stops for saving to file.
TWEETS_DATA_PATH = '/trendingdata/twitter_data'
TRACKED_KEYWORDS = 'trailer,movie,film,dvd,cinema,episode'  # format is 'keyword1,keyword2,keyword3'


class TwitterAPI:
    """
    Author: Albin Bergvall
    Date: 2017-11-20
    Purpose: Class responsible for saving twitter data to the file system
    via a stream, and also calculating a twitter trending score
    based on the data from the stream.
    """

    def __init__(self):
        self.all_words_new = {}

    @staticmethod
    def open_twitter_stream(time_limit):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-03
        Purpose: To initiate a stream against the twitter API which listens for
        new tweets corresponding to a set of movie/series related keywords.
        The stream runs on a separate thread, and the duration of the stream as well
        as how often it will save the data can be set in the TwitterAPI.py file.
        :return:
        """
        output_stream = StdOutListener(time_limit)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        stream = Stream(auth, output_stream)
        try:
            stream.filter(track=[TRACKED_KEYWORDS], languages=['en'], async=True)
        except:
            print("An error occurred. The twitter stream has been terminated.")

    def get_twitter_score(self, title):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-05
        Purpose: To score a movie/series title based on the number of times each word
        in the title is mentioned in tweets. This method does not require a background model.
        :param title:
        :return twitter_score:
        """
        if not self.all_words_new:
            self.load_new_dict()
        title = title.lower()
        twitter_score = None
        words = title.split()
        for word in words:
            word = self.format_word(word)
            twitter_score = self.get_word_score(word, twitter_score, self.all_words_new)
        return twitter_score

    @staticmethod
    def get_word_score(word, score, word_dict):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-05
        Purpose: This function is used to determine how many times
        a certain word has been mentioned.
        It will also compare the score to an already set score,
        and choose the one with fewer mentions.
        This is to give a score based on keyword mentions of the entire title.
        :param word:
        :param score:
        :param word_dict:
        :return:
        """
        if word in word_dict:
            curr_score = word_dict.get(word)
            if score is None:
                score = curr_score
            elif curr_score < score:
                score = curr_score
        else:
            score = 0
        return score

    def load_new_dict(self):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-13
        Purpose: The purpose of this function is to load a saved dictionary from the file system.
        The file loaded will be the latest modified one.
        :return:
        """
        try:
            latest_file = self.get_newest_file()
            if os.path.getsize(latest_file) < 1500:
                os.remove(latest_file)
                self.load_new_dict()
            else:
                with open(latest_file, 'rb') as f:
                    self.all_words_new = pickle.load(f)
        except (TypeError, FileNotFoundError, EOFError):
            print("File could not be loaded into dictionary for twitter score calculations.")

    @staticmethod
    def get_newest_file():
        """
        Author: Albin Bergvall
        Date: 2017-11-13
        Purpose: The purpose of this function is to load the latest modified file from
        the trendingdata directory. Used for loading dictionaries and to check if files exist.
        :return:
        """
        path = os.path.dirname(os.path.abspath(__file__)) + '/trendingdata/*.bin'
        list_of_files = glob.iglob(path)
        try:
            latest_file = max(list_of_files, key=os.path.getctime)
            return latest_file
        except ValueError:
            return None

    @staticmethod
    def remove_old_dict():
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-20
        Purpose: Remove datafiles in Trending data folder that are older than seven days.
        :return:
        """
        path = os.path.dirname(os.path.abspath(__file__)) + '/trendingdata'
        now = time.time()
        for file in os.listdir(path):
            file = os.path.join(path, file)
            if os.stat(file).st_mtime < (now - 7 * 86400):
                if os.path.isfile(file):
                    os.remove(file)

    @staticmethod
    def format_word(word):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-13
        Purpose: To take a word as a parameter, format and return it
        so that it will be of same format as words stored from twitter stream.
        :param word:
        :return:
        """
        word = word.lower()
        word = word.strip(" ")
        regex = re.compile('[^a-z0-9]')
        word = regex.sub('', word)
        if word == "" or word.startswith("httpstco"):
            return None
        return word


class StdOutListener(StreamListener):
    """
    Author: Albin Bergvall, Karl Lundvall
    Date: 2017-11-20
    Listener class used for twitter stream. Function on_status is called
    each time a tweet corresponding to a set of keywords is picked up by stream.
    Also contains functions for formatting words, saving them to a dictionary and
    lastly saving the dictionary to the file system.
    """

    def __init__(self, limit):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-13
        Purpose: Constructor for the stream class.
        Takes time limit for the stream as parameter
        for when it should be terminated.
        :param limit: time for stream uptime in seconds
        """
        self.start_time = time.time()
        self.limit = limit
        self.all_words = {}
        super(StdOutListener, self).__init__()
        print("Twitter stream has been started")

    def on_status(self, status):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-13
        Purpose: This function is called each time a tweet is picked up by the filter.
        It checks if time limits has been exceeded for saving to file,
        and also takes the tweet text, splits it, and then calls other functions for
        formatting and saving the words to a dictionary.
        :param status:
        :return:
        """
        if(time.time() - self.start_time) < self.limit:
            words = status.text.split()
            for word in words:
                word = self.format_word(word)
                if word is not None:
                    self.update_count(word)
            return True
        self.store_dict()
        return False

    @staticmethod
    def format_word(word):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-13
        Purpose: To take a word as a parameter, format it and return the word
        if there is anything left after doing a regex check over the characters of the word.
        Otherwise, return None.
        :param word:
        :return word:
        """
        word = word.lower()
        word = word.strip(" ")
        regex = re.compile('[^a-z0-9]')
        word = regex.sub('', word)
        if word == "" or word.startswith("httpstco"):
            return None
        return word

    def on_error(self, status):
        """
        Author: Albin Bervall, Karl Lundvall
        Date: 2017-11-13
        Purpose: Function which is called if there was an error with the stream.
        Saves the dictionary and closes stream.
        :param status:
        :return:
        """
        self.store_dict()
        print(status)

    def update_count(self, word):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-13
        Purpose: To save a word to the dictionary if it hasn't been mentioned yet,
        otherwise increase the count of an already mentioned word.
        :param word:
        :return:
        """
        if word in self.all_words:
            val = self.all_words.get(word)
            val += 1
            self.all_words[word] = val
        else:
            self.all_words[word] = 1

    def store_dict(self):
        """
        Author: Albin Bergvall, Karl Lundvall
        Date: 2017-11-13
        Purpose: To save a dictionary to a file in the trendingdata folder.
        The name of the file will include the date of when it was saved.
        This way, we will know from which day data was stored.
        :return:
        """
        try:
            path = os.path.dirname(os.path.abspath('__file__')) + TWEETS_DATA_PATH \
                   + datetime.datetime.today().strftime('%Y%m%d') + ".bin"
            with open(path, 'wb') as file:
                pickle.dump(self.all_words, file, pickle.HIGHEST_PROTOCOL)
                file.close()
        except FileNotFoundError:
            path = os.path.dirname(os.path.abspath(__file__)) + TWEETS_DATA_PATH \
                   + datetime.datetime.today().strftime('%Y%m%d') + ".bin"
            with open(path, 'wb') as file:
                pickle.dump(self.all_words, file, pickle.HIGHEST_PROTOCOL)
                file.close()
        print("Dictionary saved to file! Path:", path)
        print("Removing old dictionaries...")
        try:
            if os.environ["REMOVETWITTERFILES"] == "1":
                TwitterAPI.remove_old_dict()
        except KeyError:
            pass

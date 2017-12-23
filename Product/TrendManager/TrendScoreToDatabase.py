"""
Author: John Andree Lidquist, Marten Bolin
Date:
Last update: 2017/11/21 Albin Bergvall
Purpose: Gets movie from database and stores a trending score
"""

from datetime import datetime
import threading
import os
from apscheduler.schedulers.background import BackgroundScheduler

from Product.TrendManager.TwitterAPI import TwitterAPI
from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DatabaseManager.Insert.InsertTrending import InsertTrending
from Product.Database.DatabaseManager.Retrieve.RetrieveTrending import RetrieveTrending
from Product.Database.DatabaseManager.Update.UpdateTrending import UpdateTrending
from Product.TrendManager.TrendingController import TrendingController

TIME_LIMIT_TWITTER_STREAM = 43200  # Time limit for twitter stream uptime in seconds
# Time limit for twitter stream if there is no file to load data from
TIME_LIMIT_TWITTER_STREAM_NO_FILE = 7200


class TrendingToDB(object):
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-12
    Last update: 2017-11-13
    Purpose: This class handles collecting all the trending scores so that they can
    be stored in the database.
    The class is using threads and will be abel to run in the background continuously
    """
    def __init__(self, daemon=False, daily=False):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date:2017-10-12
        Last update: 2017-11-17
        Purpose: Instantiates the class, and based on the params an be run in different ways.
        :param daemon: True - makes the process terminate when app is finished.
        False - The process will not terminate until finished or terminated.
        :param daily: True - Will make the process run once every day.
        False - Will only run the process once.
        """
        # self.daemon = daemon
        self.stop = False
        self.daily = daily
        self.insert_trend = InsertTrending()
        self.retrieve_trend = RetrieveTrending()
        self.alter_trend = UpdateTrending()
        self.retrieve_movie = RetrieveMovie()

        if daily:
            # if set to daily, it creates a scheduler and sets the interval to 1 day
            self.scheduled = BackgroundScheduler()
            if not daemon:
                self.scheduled._daemon = False
            self.scheduled.add_job(self.run, 'interval', days=1, id="1")
            self.scheduled.start()
            self.scheduled.modify_job(job_id="1", next_run_time=datetime.now())
        else:
            # creates the thread that will make the method run parallel.
            # Sets daemon to true so that it will allow
            # the app to be terminated and will terminate with it.
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = daemon
            thread.start()

    def run(self):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 2017-10-28
        Last update:2017-11-21 Albin Bergvall
        Purpose: The method where which will fetch all the scores by the
        TrendingController which communicate with the Youtube and Twitter API.
        """

        # Following steps are done:
        # 1. Query movies from database
        # 2. Get new score for that movie
        # 3. Save the highest scores from the different trending sources
        # 4. Iterate though list of scored movies and normalize,
        # weight and add the scores to a total score
        # 5. If current total score is different from the newly
        # fetched score - Update score in database, else go to step 1
        # 6. Go to step 1

        trend_controller = TrendingController()
        res_movie = self.retrieve_movie.retrieve_movie()
        scored_movies = []
        twitter_max = 1
        youtube_max = 1

        for movie in res_movie:
            if self.stop:
                break

            scored_movie = trend_controller.get_trending_content(movie.title)
            scored_movie.id = movie.id

            if scored_movie.youtube_score > youtube_max:
                youtube_max = scored_movie.youtube_score
            if scored_movie.twitter_score > twitter_max:
                twitter_max = scored_movie.twitter_score

            scored_movies.append(scored_movie)
            print("Movie ID:", scored_movie.id)

        print("Inserting scored movies into database...")
        for scored_movie in scored_movies:
            res_score = self.retrieve_trend.retrieve_trend_score(scored_movie.id)

            scored_movie.total_score = (scored_movie.youtube_score * 0.7 / youtube_max) + \
                                       (scored_movie.twitter_score * 0.3 / twitter_max)
            if res_score:

                if scored_movie.total_score != res_score.total_score:
                    # If score is new
                    self.alter_trend.update_trend_score(movie_id=scored_movie.id,
                                                        total_score=scored_movie.total_score,
                                                        youtube_score=scored_movie.youtube_score,
                                                        twitter_score=scored_movie.twitter_score)
            else:
                # If movie is not in TrendingScore table
                self.insert_trend.add_trend_score(movie_id=scored_movie.id,
                                                  total_score=scored_movie.total_score,
                                                  youtube_score=scored_movie.youtube_score,
                                                  twitter_score=scored_movie.twitter_score)

                # The commit is in the loop for now due to high waiting time but
                # could be moved outside to lower total run time

        # Open twitter stream after titles has been scored, to gather new data
        # The os.environ checks if the run config has a variable named "TWITTERSTREAM"
        # and only starts stream if it is set to 1. This is to make sure that the stream
        # isn't opened during testing.
        try:
            if os.environ["TWITTERSTREAM"] == "1":
                TwitterAPI().open_twitter_stream(TIME_LIMIT_TWITTER_STREAM)
                print("Opened Twitter Stream")
        except KeyError:
            pass
        print("Waiting until next day to update")

    # Used to stop the thread if background is false
    # or for any other reason it needs to be stopped.
    def terminate(self):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date:
        Last update:
        Purpose: Terminates the process
        """
        print("Shutting down TrendScoreToDatabase")
        self.stop = True
        if self.daily:
            self.scheduled.shutdown()

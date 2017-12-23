"""
Unit tests for TwitterAPI.py
"""

from ..TwitterAPI import TwitterAPI


def test_get_word_score():
    """
    Author: Karl Lundvall
    Date: 2017-11-13
    Purpose: Assert that it is possible to retrieve a score
    from the dictionary and that the score is an integer.
    """
    # Pre-conditions
    twitter_api = TwitterAPI()
    dictionary = {'Batman': 0}
    word = 'Batman'

    # Expected output
    expected1 = 0
    expected2 = int(expected1)

    # Observed output
    observed = twitter_api.get_word_score(word, 0, dictionary)
    observed1 = twitter_api.get_word_score(word, 0, dictionary)

    assert observed is expected1
    assert observed1 is expected2


def test_format_word():
    """
    Author: Karl Lundvall
    Date: 2017-11-13
    Purpose: Assert that words are in lowercase and that
    all non alphabetic or numeric characters gets removed.
    """
    # Pre-conditions
    twitter_api = TwitterAPI()

    # Expected output
    expected = "hej"

    # Observed output
    observed = twitter_api.format_word("H*E'?J")

    assert observed == expected


def test_load_dict():
    """
    Author: Karl Lundvall
    Date: 2017-11-13
    Purpose: Assert that print_dict retrieves a dictionary from the twitter_dataYYYYMMDD.bin.
    """
    # Pre-conditions
    twitterapi = TwitterAPI()

    # Observed output
    twitterapi.load_new_dict()

    assert twitterapi.all_words_new is not None


def test_get_twitter_score():
    """
    Author: Karl Lundvall
    Date: 2017-11-13
    Purpose: Assert that get_twitter_score retrieves a score.
    """
    # Pre-conditions
    twitter_api = TwitterAPI()

    # Observed output
    observed = twitter_api.get_twitter_score("rt")

    assert observed > 0


def test_get_newest_file():
    """
    Author: Albin Bergvall
    Date: 2017-11-20
    Purpose: Assert that get_newest_file returns a file
    from the twitterdata directory, if the file exists
    """
    # Pre-conditions
    twitter_api = TwitterAPI()

    # Observed outputs
    observed = twitter_api.get_newest_file()

    assert observed is not None


""" - Not really testable
def test_open_twitter_stream():  # NOT DONE

    Author: Alin Bergvall
    Date: 2017-11-15
    Purpose: Assert that the twitter stream opens and saves file to system
    :return:
    # Pre-conditions
    # twitter_api = TwitterAPI()

    # Observed output
    # twitter_api.open_twitter_stream()
"""

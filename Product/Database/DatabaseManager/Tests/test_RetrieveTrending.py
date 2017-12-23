"""
Test file to test RetrieveTrending.py
"""
from Product.Database.DatabaseManager.Retrieve.RetrieveTrending import RetrieveTrending
from Product.Database.DBConn import create_session
from Product.Database.DBConn import TrendingScore
from Product.Database.DBConn import Movie


def test_retrieve_trend_score():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Latest Update: 2017-11-20
    Purpose: Assert that trend total_score is retrieved from the database correctly
    """

    # PRE-CONDITIONS
    movie_id = -1
    total_score = 9999999999999
    youtube_score = 10
    twitter_score = 20

    # We create a session and add a dummy movie and a dummy total score
    # Two commits are necessary because of foreign constraints
    session = create_session()
    dummy_movie = Movie(id=movie_id, title='Dummy', year=1111)
    dummy_score = TrendingScore(movie_id=movie_id, total_score=total_score,
                                youtube_score=youtube_score, twitter_score=twitter_score)
    session.add(dummy_movie)
    session.commit()
    session.add(dummy_score)
    session.commit()

    # EXPECTED OUTPUT
    expected_movie_id = movie_id
    expected_total_score = total_score
    expected_youtube_score = youtube_score
    expected_twitter_score = twitter_score

    # OBSERVED OUTPUT
    # We call the method to be tested that retrieves all the users
    observed_score = RetrieveTrending().retrieve_trend_score(movie_id=movie_id)
    observed_score_five = RetrieveTrending().retrieve_trend_score(number_of_titles=5)
    observed_score_all = RetrieveTrending().retrieve_trend_score()
    observed_total_score = observed_score.total_score

    observed_movie_id_1 = None
    observed_total_score_1 = None
    observed_youtube_score_1 = None
    observed_twitter_score_1 = None
    observed_movie_id_2 = None
    observed_total_score_2 = None
    observed_youtube_score_2 = None
    observed_twitter_score_2 = None

    for rating in observed_score_five:
        if rating.movie_id == movie_id:
            observed_movie_id_1 = rating.movie_id
            observed_total_score_1 = rating.total_score
            observed_youtube_score_1 = rating.youtube_score
            observed_twitter_score_1 = rating.twitter_score
            break

    for rating in observed_score_all:
        if rating.movie_id == movie_id:
            observed_movie_id_2 = rating.movie_id
            observed_total_score_2 = rating.total_score
            observed_youtube_score_2 = rating.youtube_score
            observed_twitter_score_2 = rating.twitter_score
            break

    # After adding the dummy user we remove them again.
    # Two commits are necessary because of foreign constraints
    session.delete(dummy_score)
    session.commit()
    session.delete(dummy_movie)
    session.commit()
    session.close()

    assert observed_score
    assert observed_total_score == expected_total_score

    assert observed_score_five
    assert observed_movie_id_1 == expected_movie_id
    assert observed_total_score_1 == expected_total_score
    assert observed_youtube_score_1 == expected_youtube_score
    assert observed_twitter_score_1 == expected_twitter_score

    assert observed_score_all
    assert observed_movie_id_2 == expected_movie_id
    assert observed_total_score_2 == expected_total_score
    assert observed_youtube_score_2 == expected_youtube_score
    assert observed_twitter_score_2 == expected_twitter_score


def test_get_trending_twitter():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Purpose: Assert that trend twitter_score is retrieved from the database correctly
    """

    # PRE-CONDITIONS
    movie_id = -1
    total_score = 10
    youtube_score = 20
    twitter_score = 999999999999

    # We create a session and add a dummy movie and a dummy total score
    # Two commits are necessary because of foreign constraints
    session = create_session()
    dummy_movie = Movie(id=movie_id, title='Dummy', year=1111)
    dummy_score = TrendingScore(movie_id=movie_id, total_score=total_score,
                                youtube_score=youtube_score, twitter_score=twitter_score)
    session.add(dummy_movie)
    session.commit()
    session.add(dummy_score)
    session.commit()

    # EXPECTED OUTPUT
    expected_movie_id = movie_id
    expected_total_score = total_score
    expected_youtube_score = youtube_score
    expected_twitter_score = twitter_score

    # OBSERVED OUTPUT
    # We call the method to be tested that retrieves all the users
    observed_scores = RetrieveTrending().get_trending_twitter(num_of_titles=5)

    observed_movie_id = None
    observed_total_score = None
    observed_youtube_score = None
    observed_twitter_score = None

    for rating in observed_scores:
        if rating.movie_id == movie_id:
            observed_movie_id = rating.movie_id
            observed_total_score = rating.total_score
            observed_youtube_score = rating.youtube_score
            observed_twitter_score = rating.twitter_score
            break

    # After adding the dummy user we remove them again.
    # Two commits are necessary because of foreign constraints
    session.delete(dummy_score)
    session.commit()
    session.delete(dummy_movie)
    session.commit()
    session.close()

    assert observed_scores
    assert observed_movie_id == expected_movie_id
    assert observed_total_score == expected_total_score
    assert observed_youtube_score == expected_youtube_score
    assert observed_twitter_score == expected_twitter_score


def test_get_trending_youtube():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Purpose: Assert that trend youtube_score is retrieved from the database correctly
    """
    # PRE-CONDITIONS
    movie_id = -1
    total_score = 10
    youtube_score = 99999999999
    twitter_score = 20

    # We create a session and add a dummy movie and a dummy total score
    # Two commits are necessary because of foreign constraints
    session = create_session()
    dummy_movie = Movie(id=movie_id, title='Dummy', year=1111)
    dummy_score = TrendingScore(movie_id=movie_id, total_score=total_score,
                                youtube_score=youtube_score, twitter_score=twitter_score)
    session.add(dummy_movie)
    session.commit()
    session.add(dummy_score)
    session.commit()

    # EXPECTED OUTPUT
    expected_movie_id = movie_id
    expected_total_score = total_score
    expected_youtube_score = youtube_score
    expected_twitter_score = twitter_score

    # OBSERVED OUTPUT
    # We call the method to be tested that retrieves all the users
    observed_scores = RetrieveTrending().get_trending_youtube(num_of_titles=5)

    observed_movie_id = None
    observed_total_score = None
    observed_youtube_score = None
    observed_twitter_score = None

    for rating in observed_scores:
        if rating.movie_id == movie_id:
            observed_movie_id = rating.movie_id
            observed_total_score = rating.total_score
            observed_youtube_score = rating.youtube_score
            observed_twitter_score = rating.twitter_score
            break

    # After adding the dummy user we remove them again.
    # Two commits are necessary because of foreign constraints
    session.delete(dummy_score)
    session.commit()
    session.delete(dummy_movie)
    session.commit()
    session.close()

    assert observed_scores
    assert observed_movie_id == expected_movie_id
    assert observed_total_score == expected_total_score
    assert observed_youtube_score == expected_youtube_score
    assert observed_twitter_score == expected_twitter_score

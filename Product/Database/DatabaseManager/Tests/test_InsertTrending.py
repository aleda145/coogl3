"""
Test file to test InsertTrending.py
"""
from Product.Database.DatabaseManager.Insert.InsertTrending import InsertTrending
from Product.Database.DBConn import create_session
from Product.Database.DBConn import TrendingScore
from Product.Database.DBConn import Movie


def test_add_trend_score():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Purpose: Assert that trend scores are inserted to the database correctly
    """

    # PRE-CONDITIONS
    movie_id = -1
    total_score = 10
    youtube_score = 20
    twitter_score = 30

    # We create a session and add a dummy movie to add a score to
    session = create_session()
    dummy_movie = Movie(id=movie_id, title="dummy", year=1111)
    session.add(dummy_movie)
    session.commit()

    # We use the method to be tested and add a score to the dummy movie
    InsertTrending().add_trend_score(movie_id=movie_id, total_score=total_score,
                                     youtube_score=youtube_score, twitter_score=twitter_score)

    # EXPECTED OUTPUT
    # The expected output are the same variables as the Pre-conditions

    # OBSERVED OUTPUT
    # We query the the score to get a observed output
    observed = session.query(TrendingScore).filter_by(movie_id=movie_id).first()

    # After adding the dummy movie and the dummy trending score for it, we remove them again.
    # We need to commit twice because of foreign key constraints
    session.delete(observed)
    session.commit()
    session.delete(dummy_movie)
    session.commit()
    session.close()

    assert observed
    assert observed.movie_id == movie_id
    assert observed.total_score == total_score
    assert observed.youtube_score == youtube_score
    assert observed.twitter_score == twitter_score

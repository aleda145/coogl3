"""
Test file to test UpdateTrending.py
"""
from Product.Database.DatabaseManager.Update.UpdateTrending import UpdateTrending
from Product.Database.DBConn import create_session
from Product.Database.DBConn import Movie
from Product.Database.DBConn import TrendingScore


def test_update_trend_score():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Last Updated:
    Purpose: Assert that trend scores are updated in the database correctly
    """

    # PRE-CONDITIONS
    movie_id = -1
    score_before_update = 10
    score_after_update = 20

    # We create a session and add a dummy movie and a dummy trending score for that movie
    session = create_session()
    dummy_movie = Movie(id=movie_id, title="dummy", year=1111)
    session.add(dummy_movie)
    session.commit()
    dummy_score = TrendingScore(movie_id=movie_id, total_score=score_before_update,
                                youtube_score=score_before_update,
                                twitter_score=score_before_update)
    session.add(dummy_score)
    session.commit()

    # We use the method to be tested and update to the new score
    UpdateTrending().update_trend_score(movie_id=movie_id, total_score=score_after_update,
                                        youtube_score=score_after_update,
                                        twitter_score=score_after_update)

    # EXPECTED OUTPUT
    expected_score = score_after_update

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
    assert observed.total_score == expected_score
    assert observed.youtube_score == expected_score
    assert observed.twitter_score == expected_score

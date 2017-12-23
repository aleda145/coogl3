"""
Test file to test InsertRecommendation.py
"""
from Product.Database.DatabaseManager.Insert.InsertRecommendation import InsertRecommendation
from Product.Database.DBConn import create_session
from Product.Database.DBConn import User
from Product.Database.DBConn import Movie
from Product.Database.DBConn import Recommendation


def test_insert_recommendation():
    """
    Author: John Andree Lidquist
    Date: 2017-11-15
    Last Updated: 2017-11-16
    Purpose: Assert that recommendations are inserted to the database
    """

    # PRE-CONDITIONS
    movie_id_1 = -1
    movie_id_2 = -2
    user_id = -1

    # We create a session and add a two dummy movies and a dummy user
    session = create_session()
    dummy_movie_1 = Movie(id=movie_id_1, title="dummy1", year=1111)
    dummy_movie_2 = Movie(id=movie_id_2, title="dummy2", year=1111)
    dummy_user = User(id=user_id, age=10, gender='Male', occupation='Student')
    session.add(dummy_movie_1)
    session.add(dummy_movie_2)
    session.add(dummy_user)
    session.commit()

    # We make the recommendation of the two dummy movies to the dummy user
    movie_list = [{'id': movie_id_1}, {'id': movie_id_2}]
    InsertRecommendation().insert_recommendation(movie_list=movie_list, user_id=user_id)

    # EXPECTED OUTPUT
    # The expected output are the same variables as the Pre-conditions

    # OBSERVED OUTPUT
    # We query the recommendations to get an observed output
    observed_1 = session.query(Recommendation).filter_by(movie_id=movie_id_1,
                                                         user_id=user_id).first()
    observed_2 = session.query(Recommendation).filter_by(movie_id=movie_id_2,
                                                         user_id=user_id).first()

    # After adding the dummy movies, the dummy user and the dummy recommendation,
    # we remove them again. We need to commit twice because of foreign key constraints
    session.delete(observed_1)
    session.delete(observed_2)
    session.commit()
    session.delete(dummy_movie_1)
    session.delete(dummy_movie_2)
    session.delete(dummy_user)
    session.commit()
    session.close()

    assert observed_1
    assert observed_1.movie_id == movie_id_1
    assert observed_1.user_id == user_id
    assert observed_2
    assert observed_2.movie_id == movie_id_2
    assert observed_2.user_id == user_id

"""
Test file to test InsertFeedback.py
"""
from Product.Database.DatabaseManager.Insert.InsertFeedback import InsertFeedback
from Product.Database.DBConn import create_session
from Product.Database.DBConn import User
from Product.Database.DBConn import Movie
from Product.Database.DBConn import Rating
from Product.Database.DBConn import Recommendation


def test_insert_feedback():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-21
    Last Updated: 2017-11-21
    Purpose: Assert that feedback is inserted to the database
    """

    # PRE-CONDITIONS
    user_id_1 = -1
    user_id_2 = -2
    user_id_3 = -3
    movie_id = -1
    rating_new = 1.5
    rating_update = 2.5
    watched = False

    # We create a session and add a dummy movie and a dummy user
    # We need to commit twice because of foreign key constraints
    session = create_session()
    dummy_movie = Movie(id=movie_id, title="dummy", year=1111)
    dummy_user_1 = User(id=user_id_1, age=10, gender='Male', occupation='Student')
    dummy_user_2 = User(id=user_id_2, age=10, gender='Male', occupation='Student')
    dummy_user_3 = User(id=user_id_3, age=10, gender='Male', occupation='Student')
    session.add(dummy_movie)
    session.add(dummy_user_1)
    session.add(dummy_user_2)
    session.add(dummy_user_3)
    session.commit()
    dummy_recommendation = Recommendation(user_id=user_id_2, movie_id=movie_id, watched=watched)
    dummy_rating = Rating(user_id=user_id_3, movie_id=movie_id, rating=rating_update)
    session.add(dummy_recommendation)
    session.add(dummy_rating)
    session.commit()

    # We call the function to be tested and let it add feedback. Three cases will be tested
    InsertFeedback().insert_feedback(user_id_1, movie_id, True, rating_new)
    InsertFeedback().insert_feedback(user_id_2, movie_id, True)
    InsertFeedback().insert_feedback(user_id_3, movie_id, True, 5.0)

    # EXPECTED OUTPUT
    expected_user_id = user_id_1
    expected_movie_id = movie_id
    expected_rating_new = rating_new
    expected_watched = True
    expected_rating_update = 5.0

    # OBSERVED OUTPUT
    # We query the rating and recommendation to get an observed output
    observed_1 = session.query(Rating).filter_by(movie_id=movie_id, user_id=user_id_1).first()
    observed_rating_new = observed_1.rating
    observed_movie_id = observed_1.movie_id
    observed_user_id = observed_1.user_id
    observed_2 = session.query(Recommendation).filter_by(movie_id=movie_id,
                                                         user_id=user_id_2).first()
    observed_watched = observed_2.watched
    observed_3 = session.query(Rating).filter_by(movie_id=movie_id, user_id=user_id_3).first()
    observed_rating_update = observed_3.rating

    # After adding the dummy movie and the dummy users, we remove them again.
    # We need to commit twice because of foreign key constraints
    session.delete(observed_1)
    session.delete(dummy_recommendation)
    session.delete(dummy_rating)
    session.commit()
    session.delete(dummy_movie)
    session.delete(dummy_user_1)
    session.delete(dummy_user_2)
    session.delete(dummy_user_3)
    session.commit()
    session.close()

    assert observed_1
    assert observed_rating_new == expected_rating_new
    assert observed_movie_id == expected_movie_id
    assert observed_user_id == expected_user_id
    assert observed_watched == expected_watched
    assert observed_rating_update == expected_rating_update

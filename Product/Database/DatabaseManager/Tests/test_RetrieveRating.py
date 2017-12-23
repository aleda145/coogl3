"""
Test file to test RetrieveRating.py
"""
from Product.Database.DatabaseManager.Retrieve.RetrieveRating import RetrieveRating
from Product.Database.DBConn import create_session
from Product.Database.DBConn import Movie
from Product.Database.DBConn import User
from Product.Database.DBConn import Rating


def test_retrieve_rating():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-16
    Last Updated:
    Purpose: Assert that a rating is retrieved correctly
    """

    # PRE-CONDITIONS
    user_id = -1
    movie_id = -1
    rating = 10

    # We create a session and add a dummy movie, a dummy user and a dummy rating for
    # that user and movie
    session = create_session()
    dummy_movie = Movie(id=movie_id, title="dummy", year=1111)
    dummy_user = User(id=user_id, age=10, gender='Male', occupation='Student')
    session.add(dummy_movie)
    session.add(dummy_user)
    session.commit()
    dummy_rating = Rating(user_id=user_id, movie_id=movie_id, rating=rating)
    session.add(dummy_rating)
    session.commit()

    # EXPECTED OUTPUT
    expected_rating = rating

    # OBSERVED OUTPUT
    # We call the method to be tested to get all the ratings
    observed_all_ratings = RetrieveRating().retrieve_ratings()

    # We make sure the dummy rating is part of all those ratings (the for-loop will only run once,
    # because the rating added will be first in the list
    observed_rating = 0
    for rating in observed_all_ratings:
        if rating.user_id == user_id and rating.movie_id == movie_id:
            observed_rating = rating.rating
            break

    # After adding the dummy movie, the dummy user and the dummy rating, we remove them again.
    # We need to commit twice because of foreign key constraints
    session.delete(dummy_rating)
    session.commit()
    session.delete(dummy_user)
    session.delete(dummy_movie)
    session.commit()
    session.close()

    assert observed_all_ratings
    assert observed_rating == expected_rating

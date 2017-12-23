"""
Test file to test RetrieveMovie.py
"""
from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DBConn import create_session
from Product.Database.DBConn import Movie


def test_retrieve_movie():
    """
    Author: John Andree Lidquist
    Date: 2017-11-16
    Last Updated:
    Purpose: Assert that a movie, or all movies, are retrieved correctly
    """

    # PRE-CONDITIONS
    movie_id = -1
    movie_title = "dummy"
    movie_year = 1111

    # We create a session and add a dummy movie that we can later retrieve
    session = create_session()
    dummy_movie = Movie(id=movie_id, title=movie_title, year=movie_year)
    session.add(dummy_movie)
    session.commit()  # We need to close the session, else we get an error when trying to delete it
    session.close()
    # EXPECTED OUTPUT
    expected_id = movie_id
    expected_title = movie_title
    expected_year = movie_year

    # OBSERVED OUTPUT
    # We call the method to be tested to get 1) The movie we added above, and 2) All the movies
    # which is done by not setting the parameter "movie_id"
    retrieve_movie = RetrieveMovie()
    observed_one_movie = retrieve_movie.retrieve_movie(movie_id=movie_id)
    observed_all_movies = retrieve_movie.retrieve_movie()

    # After adding the dummy movie  we remove them again.
    session.delete(observed_one_movie)
    session.commit()
    session.close()

    assert observed_one_movie
    assert observed_one_movie.id == expected_id
    assert observed_one_movie.title == expected_title
    assert observed_one_movie.year == expected_year
    assert observed_all_movies

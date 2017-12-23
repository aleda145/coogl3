"""
Test file to test files in DBFillMovies.py
"""
from Product.Database.DBConn import Movie
from Product.Database.DBConn import Genre
from Product.Database.DBConn import MovieInGenre
from Product.Database.DBConn import create_session

# This is the file to unit test the four DBFill files (DBFillUsers, DBFillMovies, DBFillRatings,
# DBFillLinks). Before the test is run the db should have been created and the four files runned
# (you can do this by running the "DBFillMovieLens" or "DBFillSmallSet" which will run the
# four files). This test will make sure that the first and last entries in the corresponding csv
# files has been successfully entered into the db. We check this by doing queries and asserting the
# result is the expected.


def test_db_fill_movies():
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-11
    Last Updated:
    Purpose: Assert that movies are loaded into the database correctly
    """
    session = create_session()
    result = session.query(Genre).filter_by(name='Action').first()
    assert result.name == 'Action'

    result = session.query(Movie).filter_by(id=1).first()
    assert result.title == "Toy Story"
    assert result.year == 1995

    result = session.query(MovieInGenre).filter_by(movie_id=1).all()
    for counter, res in enumerate(result):
        if counter == 0:
            assert res.genre == "Adventure"
        if counter == 1:
            assert res.genre == "Animation"
        if counter == 2:
            assert res.genre == "Children"
        if counter == 3:
            assert res.genre == "Comedy"
        if counter == 4:
            assert res.genre == "Fantasy"
    session.close()

"""
Test file to test files in DBFillRatings.py
"""

from Product.Database.DBConn import Rating
from Product.Database.DBConn import create_session

# This is the file to unit test the four DBFill files (DBFillUsers, DBFillMovies, DBFillRatings,
# DBFillLinks). Before the test is run the db should have been created and the four files runned
# (you can do this by running the "DBFillMovieLens" or "DBFillSmallSet" which will run the
# four files). This test will make sure that the first and last entries in the corresponding csv
# files has been successfully entered into the db. We check this by doing queries and asserting the
# result is the expected.


def test_db_fill_ratings():
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-11
    Last Updated:
    Purpose: Assert that ratings are loaded into the database correctly
    """
    session = create_session()
    result = session.query(Rating).filter_by(user_id=1, movie_id=13).first()
    session.close()
    assert result.rating == 5.0

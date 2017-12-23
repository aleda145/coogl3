"""
Class for retrieving success rate from database
"""
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import Rating


class RetrieveRating(Retrieve):
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-14
    Last update: 2017-11-22
    Purpose: Retrieve data from rating table in database
    """
    # TODO the logic to get 80% or 10% of the ratings should be done here and not in gets_from_db
    def retrieve_ratings(self, user_id=None, movie_id=None):
        # TODO add docstring
        if user_id and movie_id:
            ratings = self.session.query(Rating).filter_by(user_id=user_id, movie_id=movie_id).all()
        elif user_id:
            ratings = self.session.query(Rating).filter_by(user_id=user_id).all()
        elif movie_id:
            ratings = self.session.query(Rating).filter_by(movie_id=movie_id).all()
        else:
            ratings = self.session.query(Rating).all()
        self.session.close()
        return ratings

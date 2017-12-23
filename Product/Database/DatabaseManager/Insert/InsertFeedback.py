"""
Class for inserting feedback to database
"""
from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import Recommendation
from Product.Database.DBConn import Rating
from Product.Database.DBConn import Movie
from Product.Database.DBConn import User


class InsertFeedback(Insert):
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-17
    Last update: 2017-11-23
    Purpose: Make Insert of Feedback to the database
    """
    def insert_feedback(self, user_id, movie_id, watched=None, rating=None):
        """
        Author: Alexander Dahl, Marten Bolin
        Date: 2017-11-17
        Last update:
        Purpose: Make Feedback inserts to the database
        :param user_id: The id of the user that has made the rating or watched
        :type user_id: int
        :param movie_id: The id of the movie that has been rated or watched
        :type movie_id: int
        :param watched: 1 if has watched (optional)
        :type watched: int
        :param rating: the rating that was made, 1-5 (optional)
        :type rating: float
        """
        user = self.session.query(User).filter_by(id=user_id).first()
        movie = self.session.query(Movie).filter_by(id=movie_id).first()

        if not movie or not user:
            print("Heyyy")
            raise ValueError("User or Movie does not exist.")
        current_recommendation = self.session.query(Recommendation).filter_by(
                movie_id=movie_id, user_id=user_id).first()

        if watched and current_recommendation:
            current_recommendation.watched = watched
        if rating:
            current_rating = self.session.query(Rating).filter_by(
                    movie_id=movie_id, user_id=user_id).first()
            if not current_rating:
                new_rating = Rating(user_id=user_id, movie_id=movie_id, rating=rating)
                self.session.add(new_rating)
            else:
                current_rating.rating = rating

        self.session.commit()
        print('committed for user %s' % user_id)
        self.session.close()
# InsertFeedback().insert_feedback(user_id=1, movie_id=1, rating=2)

"""
Class for inserting recommendations to database
"""
from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import Recommendation


class InsertRecommendation(Insert):
    """
    Author: John Andree Lidquist
    Date: 14/11/2017
    Last update: 14/11/2017
    Purpose: Make Insert to the database that has to do with recommendations
    """
    def insert_recommendation(self, movie_list, user_id):
        """
        Author: Alexander Dahl
        Date: 2017-11-15
        Last update: 2017-11-16
        Purpose: Make Inserts to the recommendation table in the database
        :param movie_list: the movies that the user has been recommended
        :param user_id: the id of the user the recommendations are made to
        """

        for rec in movie_list:
            if not self.session.query(Recommendation).filter_by(user_id=user_id,
                                                                movie_id=rec['id']).scalar():
                new_recommendation = Recommendation(movie_id=rec['id'], user_id=user_id)
                self.session.add(new_recommendation)
        self.session.commit()
        print('committed recommendations for user %s' % user_id)
        self.session.close()

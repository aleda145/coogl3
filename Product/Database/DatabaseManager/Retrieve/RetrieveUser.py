"""
Purpose: Retrieve users from table in database
"""
from Product.Database.DBConn import User, Rating
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from sqlalchemy import desc


class RetrieveUser(Retrieve):
    """
    Author:Alexander Dahl
    Date: 2017-11-14
    Last update: 2017-11-14
    Purpose: Retrieve users from table in database
    """
    def retrieve_all_users(self):
        """
        Author: Alexander Dahl
        Date: 2017-11-14
        Last update: 2017-11-14
        Purpose: retrieve users from table
        :return users : list of class User
        """
        users = self.session.query(User).all()
        self.session.close()
        return users

    def check_if_user_in_rating(self, user_id):
        # TODO Add docstring
        # TODO Check so that rating is not null, return boolean instead of object
        # TODO write unit test for this method
        return self.session.query(Rating).filter_by(user_id=user_id).first()

    def retrieve_largest_user_id(self):
        """
        Author: Alexander Dahl, Marten Bolin
        Date: 19/11/2017
        Last update:
        Purpose: Supposed to get the user with the highest id
        :return User : a user of type User with highest id
        """
        user = self.session.query(User).order_by(desc(User.id)).limit(1).first()
        self.session.close()
        return user.id

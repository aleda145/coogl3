from Product.Database.DatabaseManager.Insert.InsertUser import InsertUser
from Product.RecommendationManager.model.create_new_model import CreateNewModel


class InsertNewUser(object):
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-17
    Last update:
    Purpose: Make Insert of Feedback to the database
    """
    @staticmethod
    def insert_user(age, gender, occupation=None):
        """
        Author: Alexander Dahl, Marten Bolin
        Date: 2017-11-17
        Last update:
        Purpose: Make Feedback inserts to the database
        :param age : The age of the user
        :type int

        :param gender : The gender of the user
        :type String
        :valid Male, Female, , Other, Unknown

        :param occupation : The occupation of the user (Optional)
        :type String

        """
        InsertUser().insert_user(age=age, gender=gender,occupation=occupation)
        # CreateNewModel.create_new_model()

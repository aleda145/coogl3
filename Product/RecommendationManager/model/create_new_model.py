"""    Author: Alexander Dahl
    Date: 2017-10-08
    Last update: 2017-10-08
    Purpose:
    This file creates a new model by calling the train model method
    in generate model. The param is the file name.
"""
import os

from Product.RecommendationManager.model import generate_model as generate_model


class CreateNewModel:
    """
    Author: Alexander Dahl, Mårten Bolin
    Date: 2017-11-22
    Last update:
    Purpose:
    This file creates a new model by calling the train model method
    in generate model.
    """

    @staticmethod
    def create_new_model():
        """
        Author: Alexander Dahl, Mårten Bolin
        Date: 2017-11-22
        Last update:
        Purpose:
        Call this function to retrain the model
        """
        path = os.path.dirname(os.path.abspath(__file__))
        generate_model.train_model(path + '/new_model.sav')
        print("Model adjusted.")

"""
Class to get the correct output structure in the
recommendation.generate_recommendation_list()
"""


class RecommendationList(object):
    """
    Author: Sebastian Maghsoudi / Alexander Dahl
    Date: 2017-11-01
    Last update: 2017-11-09 by Alexander Dahl
    Purpose: Constructor

    """
    def __init__(self, user_id, recommendation_list):
        self.user_id = user_id
        self.recommendation_list = recommendation_list

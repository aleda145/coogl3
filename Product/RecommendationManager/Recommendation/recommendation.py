"""
Recommendation Class.
"""
import os

import numpy as np

from Product.Database.DatabaseManager.Retrieve.RetrieveTrending import RetrieveTrending
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.RecommendationManager import gets_from_database as gets_from_database
from Product.RecommendationManager.Recommendation.recommendation_list import RecommendationList
from Product.RecommendationManager.model import generate_model as generate_model
from Product.Database.DatabaseManager.Insert.InsertRecommendation import InsertRecommendation


# At this point we assume that there is a file named new_model.sav
class Recommendation(object):
    """
    Author: Sebastian Maghsoudi / Alexander Dahl
    Date: 2017-11-01
    Last update: 2017-11-09 by Alexander Dahl
    Purpose:
    creates a recommendation class
    """
    def __init__(self, user_id):
        """
        Author: Sebastian Maghsoudi / Alexander Dahl
        Date: 2017-11-01
        Last update: 2017-11-13 by Alexander Dahl
        Purpose: constructor for the recommendation class

        :param user_id: a user_id
        :param size: how many movies should be recommended

        model is a lightfm model that has been saved in a folder above
        trending_content_meta is the normalized scores for trending_scores
        the number of fetched trending_content_meta is limited by the lim variable

        """
        # TODO should the class assume that there is a model named 'new_model.sav'?
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.model = generate_model.load_model(path + '/model/new_model.sav')
        self.user_id = user_id
        # right now lim is hard coded to number of movies to be recommended times 3
        # TODO create some logic for how big the limit should be
        # limit is now just 30 movies.
        self.lim = 30
        self.size = 10
        # this instantiates RetrieveTrending() class in the database manager and
        # gets limit number of TrendingScore classes.
        self.trending_content_meta = RetrieveTrending().\
            retrieve_trend_score(number_of_titles=self.lim, user_id=self.user_id)

    @staticmethod
    def normalize_user_scores(scores):
        """
        Author: Gustaf Norberg / Alexander Dahl
        Date: 2017-10-30
        Last update: 2017-10-30
        Purpose: normalizes the scores to be between 0 and 1.

        :return: list of scores
        """
        min_score = np.amin(scores)
        max_score = np.amax(scores)

        for i in range(0, len(scores)):
            scores[i] = (scores[i] - min_score)/(max_score-min_score)
        return scores

    def generate_recommendation_list(self):
        # TODO Do not recommened already viewed movies
        """
        Author: Sebastian Maghsoudi / Alexander Dahl
        Date: 2017-11-01
        Last update: 2017-11-29 by Alexander Dahl
        Purpose: Generates a recommendation list of size length for a given user.

        :return: a dictionary with user_id and a recommendation_list for that user
        example:
        {'user_id': 55, 'recommendation_list' :
        [{'title': 'It', 'score': 1.586134233975164, 'id': 24}]}
        """
        trending_id = [id.movie_id for id in self.trending_content_meta]
        # print(np.array(trending_id
        trending_score = [score.total_score for score in self.trending_content_meta]
        # normalize trending score
        norm_trending_score = self.normalize_user_scores(trending_score)
        # trending_weight is 0.5 at the moment
        # TODO document why trending weight is 0.5
        trending_weight = 0.5
        # checks if the user has ratings in the database
        # if there are no ratings the user preferences does not matter and
        # the user only gets the trendings as recommendations
        if RetrieveUser().check_if_user_in_rating(self.user_id):
            rec_list_score = self.model.predict(self.user_id, np.array(trending_id))
            norm_rec_list_score = self.normalize_user_scores(rec_list_score).tolist()
            final_rec_list_score = [rec+trending_weight*trend for rec, trend
                                    in zip(norm_rec_list_score, norm_trending_score)]
        else:
            final_rec_list_score = [trending_weight*trend for trend in norm_trending_score]
        # gets the movie titles for the movie ids
        movie_titles = [gets_from_database.get_movie_title(id.movie_id) for id
                        in self.trending_content_meta]
        # combines the movie_ids and movie_titles with the recommendation scores
        full_rec_list = list(map(list, zip(trending_id, movie_titles, final_rec_list_score)))
        # sorts the list on scores (index 2)
        sorted_rec_list = sorted(full_rec_list,
                                 key=lambda x: x[2],
                                 reverse=True)

        sorted_complete_rec_list = []
        for item in sorted_rec_list[:self.size]:
            sorted_complete_rec_list.append({'id': item[0],
                                             'title': item[1],
                                             'score': item[2]})
        # Creates an instance of InsertRecommendation that handles database insertions.
        # Calls the insert_recommendation method in it and makes the db insertion
        # This will not remove old recommendations and will add new ones.
        InsertRecommendation().insert_recommendation(user_id=self.user_id,
                                                     movie_list=sorted_complete_rec_list)
        return RecommendationList(self.user_id, sorted_complete_rec_list)

# print(Recommendation(55).generate_recommendation_list().__dict__)

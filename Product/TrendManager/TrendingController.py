"""
Author: Albin Bergvall, Martin Lundberg
Date: 2017-09-28
Last update: 2017-11/21
Purpose: TrendingController runs the API's and calculates returns the scores
"""
from Product.TrendManager.ScoredMovie import ScoredMovie
from Product.TrendManager.YoutubeAPI import YoutubeAPI
from Product.TrendManager.TwitterAPI import TwitterAPI
from googleapiclient.errors import HttpError


class TrendingController:
    """""
    Author: Albin Bergvall, Martin Lundberg
    2017-11-21
    Purpose: Class responsible for fetching the trending score from the API sources.
    """

    @staticmethod
    def get_trending_content(keyword):
        """
        Author: Albin Bergvall, Martin Lundberg
        Date: 2017-11-21
        Purpose: Takes the movie title (keyword) as a parameter and fetches score
        from the API sources and returns an instance of ScoredMovie
        :param keyword: keyword, e.g. movie title
        :return: a scored movie with youtube and twitter score
        """
        scored_movie = ScoredMovie()
        try:
            scored_movie.youtube_score = YoutubeAPI().get_youtube_score(keyword)
        except HttpError:
            print("The daily quota of youtube requests have been reached.")
        scored_movie.twitter_score = TwitterAPI().get_twitter_score(keyword)
        return scored_movie

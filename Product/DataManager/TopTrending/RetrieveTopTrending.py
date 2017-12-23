"""
Parent class for the other RetrieveTop classes. Implement using one its subclasses.
"""
from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DatabaseManager.Retrieve.RetrieveTrending import RetrieveTrending
from Product.DataManager.TopTrending.TopTrendingList import TopTrendingList


class RetrieveTopTrending:
    """
    Author: Marten Bolin / John Lidquist
    Date: 2017-11-10
    Last update: 2017-11-13 by Marten Bolin
    Purpose:
    Its subclasses should be used to retrieve the top trending content
    """
    def __init__(self):
        """
        Author: Marten Bolin / John Lidquist
        Date: 2017-11-10
        Last update:
        Purpose:
        The constructor of the RetrieveTopTrending class, creates a retrieve trendingscore
        and retrievemovie to fetch movie info and trending info.
        """
        self.trender = RetrieveTrending()
        self.movie_getter = RetrieveMovie()

    def get_title_and_score(self, list_of_trending_movies):
        """
        Author: Marten Bolin / John Lidquist
        Date: 2017-11-10
        Last update:
        Purpose:
        Used to take the movie id and retrieve its title and score. This is then put into seperate
        lists and put into the TopTrendingList class.
        :param list_of_trending_movies: the list of movie ids
        :return: a TopTrendingList
        """

        title_list = []
        score_list = []
        for entry in list_of_trending_movies:
            movie = self.movie_getter.retrieve_movie(entry.movie_id)
            title_list.append(movie.title)
            score_list.append(self.get_score(entry))
        return TopTrendingList(title_list, score_list)

    def get_score(self, entry):
        """
        Author: Marten Bolin / John Lidquist
        Date: 2017-11-10
        Last update:
        Purpose:
        This method gets overridden in RetrieveTopTrendingYoutube/Twitter
         so that the right score is added
        """
        return entry.total_score

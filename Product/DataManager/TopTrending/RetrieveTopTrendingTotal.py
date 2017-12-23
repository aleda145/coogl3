"""
RetrieveTopTrending Class
"""
from Product.DataManager.TopTrending.RetrieveTopTrending import RetrieveTopTrending


class RetrieveTopTrendingTotal(RetrieveTopTrending):
    """
    Author: Marten Bolin / John Lidquist
    Date: 2017-11-10
    Last update:
    Purpose:
    Will retrieve the top trending movies and scores regarding total score
    """
    def get_top_trending(self, number_of_titles):
        """
        Author: Marten Bolin / John Lidquist
        Date: 2017-11-10
        Last update:
        Purpose:
        Will retrieve the top trending movies and scores regarding total score
        :param number_of_titles: Integer that determines how many top trending movies to retrieve
        :return Returns a TopTrendingList

        """
        top_trend=self.trender.retrieve_trend_score(number_of_titles=number_of_titles)
        return self.get_title_and_score(top_trend)



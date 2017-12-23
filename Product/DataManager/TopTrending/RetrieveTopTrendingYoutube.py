"""
RetrieveTopTrendingYoutube Class
"""
from Product.DataManager.TopTrending.RetrieveTopTrending import RetrieveTopTrending


class RetrieveTopTrendingYoutube(RetrieveTopTrending):
    """
    Author: Marten Bolin / John Lidquist
    Date: 2017-11-10
    Last update:
    Purpose:
    Will retrieve the top trending movies and scores regarding youtube score
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
        top_trend = self.trender.get_trending_youtube(number_of_titles)
        return self.get_title_and_score(top_trend)

    def get_score(self, entry):
        """
        Author: Marten Bolin / John Lidquist
        Date: 2017-11-10
        Last update:
        Purpose:
        Will overwrite the parents get_score so that the twitter score is now added
        :param entry: The Trendscore entry that score is to be collected from
        :return Returns a score
        """
        return entry.youtube_score

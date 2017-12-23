"""
Class to update/alter data in the Trending table of the database
"""
from Product.Database.DBConn import TrendingScore
from Product.Database.DatabaseManager.Update.Update import Update


class UpdateTrending(Update):
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 9/11/2017
    Last update: 10/11/2017
    Purpose: Updates data in the trending table in the database
    """
    def update_trend_score(self, movie_id, total_score=None,
                           youtube_score=None, twitter_score=None):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 9/11/2017
        Last update: 10/11/2017
        Purpose: Updates the different trend scores of a movie
        :param movie_id : The id of the movie to update
        :param total_score : The value of the new total_score (Optional)
        :param youtube_score : The value of the new youtube_score (Optional)
        :param twitter_score : The value of the new twitter_score (Optional)
        """
        to_update = self.session.query(TrendingScore).filter_by(movie_id=movie_id).first()
        if total_score:
            to_update.total_score = total_score
        if youtube_score:
            to_update.youtube_score = youtube_score
        if twitter_score:
            to_update.twitter_score = twitter_score
        self.session.commit()
        self.session.close()

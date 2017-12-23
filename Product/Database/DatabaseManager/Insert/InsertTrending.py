"""
InsertTrending class that inserts to TrendindScore table
"""
from Product.Database.DBConn import TrendingScore
from Product.Database.DatabaseManager.Insert.Insert import Insert


class InsertTrending(Insert):
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 9/11/2017
    Last update: 10/11/2017
    Purpose: Supposed to make Insert to trending table in database
    """
    def add_trend_score(self, movie_id, total_score, youtube_score, twitter_score):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 9/11/2017
        Last update: 10/11/2017
        Purpose: Supposed to make Insert to trending table in database
        :param movie_id : the id of the movie which score will be updated
        :param total_score : the total score
        :param youtube_score : the youtube score
        :param twitter_score : the twitter score
        """
        movie = TrendingScore(movie_id=movie_id, total_score=total_score,
                              youtube_score=youtube_score,
                              twitter_score=twitter_score)
        self.session.add(movie)
        self.session.commit()
        self.session.close()

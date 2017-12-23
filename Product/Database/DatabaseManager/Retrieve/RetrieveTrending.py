"""
RetrieveTrending Class, is supposed to provide data from the Trending table in the database
"""
from sqlalchemy import desc
from sqlalchemy import and_
from sqlalchemy import func
from Product.Database.DBConn import TrendingScore
from Product.Database.DBConn import Rating
from Product.Database.DBConn import Recommendation
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve


class RetrieveTrending(Retrieve):
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 9/11/2017
    Last update: 10/11/2017
    Purpose: Supposed to Retrieve data from trending table in database
    """
    def retrieve_trend_score(self, movie_id=None, number_of_titles=None, user_id=None):
        """
        Author: John Andree Lidquist, Marten Bolin, Alexander Dahl
        Date: 9/11/2017
        Last update: 2017-11-22 by Alexander Dahl, Marten Bolin
        Purpose: Supposed to retrieve the Trending score from database
        :param movie_id : the id of the movie that should be retrieved (optional)
        :param number_of_titles : the number of titles with the highest total score to be returned
        :param user_id : The id of the user that the recommendation is for, will only return
        non-viewed or rated content (optional)
        :return TrendingScore : of type TrendingScore
        """
        if movie_id:
            trend = self.session.query(TrendingScore).filter_by(movie_id=movie_id).first()
        elif number_of_titles:
            if user_id:
                # Get the rated movies for the user in the rating table
                subquery_rating = self.session.query(Rating.movie_id).filter(
                    Rating.user_id == user_id)

                # Get the watched movies for the user in the recommendation table
                subquery_recommendation = self.session.query(Recommendation.movie_id).filter(
                    and_(Recommendation.user_id == user_id, Recommendation.watched == 1))

                # Get the trending movies that are not in the previous subqueries
                trend = self.session.query(TrendingScore).filter(
                    and_(TrendingScore.movie_id.notin_(subquery_rating),
                         TrendingScore.movie_id.notin_(subquery_recommendation))).limit(
                             number_of_titles).all()
            else:
                trend = self.session.query(TrendingScore).order_by(
                    desc(TrendingScore.total_score)).limit(number_of_titles).all()
        else:
            trend = self.session.query(TrendingScore).all()
        self.session.close()
        return trend

    def get_trending_twitter(self, num_of_titles):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 9/11/2017
        Last update:
        Purpose: Supposed to retrieve the Trending score from database
        :param num_of_titles : the number of titles with the highest twitter score to be returned
        :return TrendingScore : of type TrendingScore
        """
        query = self.session.query(TrendingScore).order_by(desc(
            TrendingScore.twitter_score)).limit(num_of_titles)
        return query

    def get_trending_youtube(self, num_of_titles):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 9/11/2017
        Last update:
        Purpose: Supposed to retrieve the Trending score from database
        :param num_of_titles : the number of titles with the highest twitter score to be returned
        :return TrendingScore : of type TrendingScore
        """
        query = self.session.query(TrendingScore).order_by(desc(
            TrendingScore.youtube_score)).limit(num_of_titles)
        return query

    def get_twitter_max(self):
        """
        Author: Linn Pettersson
        Date: 2017-11-20
        Last update:
        Purpose: Get the highest stored Twitter score
        :return: Query getting the max value from twitter_score in the database
        """
        query = self.session.query(func.max(TrendingScore.twitter_score))
        return query

    def get_youtube_max(self):
        """
        Author: Linn Pettersson
        Date: 2017-11-20
        Last update: 2017-11-20
        Purpose: Get the highest stored Youtube score
        :return: Query getting the max value from youtube_score in the database
        """
        query = self.session.query(func.max(TrendingScore.youtube_score))
        return query

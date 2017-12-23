"""
The RetrieveMovie Class is supposed to provide data about movies from database
"""
from Product.Database.DBConn import Movie
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from sqlalchemy import desc


class RetrieveMovie(Retrieve):
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 9/11/2017
    Last update: 10/11/2017
    Purpose: Supposed to Retrieve data from movie table in database
    """
    def retrieve_movie(self, movie_id=None):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 9/11/2017
        Last update: 10/11/2017
        Purpose: Supposed to query from movie table in database
        :param movie_id : the id of the movie that should be retrieved (optional) if no
        movie_id is provided all movies in the database are returned
        :return Movie : a movie of type Movie
        """
        if movie_id:
            movie = self.session.query(Movie).filter_by(id=movie_id).first()
        else:
            movie = self.session.query(Movie).all()
        self.session.close()
        return movie

    def retrieve_largest_movie_id(self):
        """
        Author: Alexander Dahl, Marten Bolin
        Date: 19/11/2017
        Last update:
        Purpose: Supposed to get the movies with the highest id
        :return Movie : a movie of type Movie with highest id
        """
        movie = self.session.query(Movie).order_by(desc(Movie.id)).limit(1).first()
        self.session.close()
        return movie.id

"""
In this file, the database is created and given a relational model
"""
import os
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, func, Date

"""
Author: John Andree Lidquist, Marten Bolin
Date: 2017-10-12
Last update: 2017-11-22
Purpose: Creates the database and the database model
"""

# Get the path and create the sqlite engine. Echo false means that we do not see generated SQL.
basedir = os.path.abspath(os.path.dirname(__file__))

try:
    PRODUCTION_DATABASE = os.environ['PRODUCTION_DATABASE'] == '1'
except KeyError:
    PRODUCTION_DATABASE = False
finally:
    if not PRODUCTION_DATABASE:
        engine = create_engine('sqlite:///' + os.path.join(basedir, 'app.db'),
                               connect_args={'check_same_thread': False}, echo=False)
        # Used to turn foreign keys on in SQLite since this is by default

        @event.listens_for(engine, "connect")
        def set_sqlite_pragma(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()
    else:
        DATABASE = os.environ["DATA_DATABASE_HOST"]
        engine = create_engine('mysql+pymysql://root:example@' + DATABASE + '/main')


# Used for the declarative part where we create the model
Base = declarative_base()


# The declarative part that describes the tables. This is and example of a User class.
# Do not forget to import type if you want to use other than integer or string
# The __repr__ returns a string that describes the object

class Genre(Base):
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: The table for movie genres
    """
    __tablename__ = 'genres'
    name = Column(String(100), primary_key=True)

    def __repr__(self):
        return "<Genre(name='%s')>" % (
            self.name)


class Movie(Base):
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: The table for movies
    """
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    year = Column(Integer)

    def __repr__(self):
        return "<Movie(id='%s', title='%s', year='%s)>" % (
            self.id, self.title, self.year)


class TrendingScore(Base):
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: The table for trending scores
    """
    __tablename__ = 'trendingscores'
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    total_score = Column(Float, default=0)
    youtube_score = Column(Float, default=0)
    twitter_score = Column(Float, default=0)

    def __eq__(self, other):
        return self == other

    def __repr__(self):
        return "<TrendingScore(movie_id='%s', total_score='%s', youtube_score='%s'," \
               "twitter_score='%s')>" % (self.movie_id, self.total_score,
                                         self.youtube_score, self.twitter_score)


class User(Base):
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: The table for users
    """
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    age = Column(Integer, default=-1)
    gender = Column(String(30), default="Unknown")
    occupation = Column(String(30), default="Unknown")

    def __repr__(self):
        return "<User(id='%s', age='%s', gender='%s', occupation='%s')>" % (
            self.id, self.age, self.gender, self.occupation)


class Rating(Base):
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: The table for ratings
    """
    __tablename__ = 'ratings'
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    rating = Column(Float)

    def __repr__(self):
        return "<Rated(user='%s', rated='%s', rating='%s')>" % (
            self.user_id, self.movie_id, self.rating)


class MovieInGenre(Base):
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: The table for linking a movie to genres
    """
    __tablename__ = 'movieingenre'
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    genre = Column(String(100), ForeignKey(Genre.name), primary_key=True)

    def __repr__(self):
        return "<Genre(movie_id='%s', genre='%s')>" % (
            self.movie_id, self.genre)


class Recommendation(Base):
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: The table for recommendations
    """
    __tablename__ = 'recommendation'
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id), primary_key=True)
    watched = Column(Integer)

    def __repr__(self):
        return "<Recommendation(user_id id='%s', movie_id ='%s', watched='%s')>" % (
            self.user_id, self.movie_id, self.watched)


class SuccessRate(Base):
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: The table for success rate
    """
    __tablename__ = 'successrate'
    id = Column(Integer, autoincrement=True, primary_key=True)
    watched = Column(Integer)
    not_watched = Column(Integer)
    average_user_success_rate = Column(Float)
    timestamp = Column(Date)

    def __repr__(self):
        return "<Recommendation(id id='%s', watched ='%s', not_watched ='%s'," \
               "average_user_success_rate='%s', timestamp='%s')>" % (self.id, self.watched,
                                                                     self.not_watched,
                                                                     self.average_user_success_rate,
                                                                     self.timestamp)


# DO NOT CHANGE BELOW
def create_session():
    """
    Author: John Andree Lidquist, Marten Bolin
    Purpose: A method to create a session which handles database queries
    """
    # Creates the tables in the database
    Base.metadata.create_all(engine)

    # Creating a session of the engine. The sessions is used for queries and inserts to db.
    # Remember to import it to the file in which you want to do such
    session = sessionmaker(bind=engine)
    return session()

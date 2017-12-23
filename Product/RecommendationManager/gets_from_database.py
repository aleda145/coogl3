"""
Handles the connections to the database
get_trending_scores puts the trending_scores from the
database in a dictionary

get_train_matrix fetches data from the database and puts
it into a training matrix for the lightFM model

get_test_matrix fetches data from the database and puts
it into a test matrix from the lightFM model

get_movie_title returns the movie title for one movie id

"""
from scipy.sparse import coo_matrix
# import random


from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DatabaseManager.Retrieve.RetrieveRating import RetrieveRating
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser

def get_train_matrix():
    """
    Author: Marten Bolin / John Lidquist
    Date: 2017-10-02
    Last update: 2017-11-14 by Alexander Dahl
    Purpose:
    returns the train matrix. The matrix is 80% (4/5) of the user ratings at the moment
    OBS! coo_matrix is a sparse matrix and will (most likely) have the same
    dimensions for train_matrix, test_matrix and new_user_matrix

    :return: training matrix in the form of a numpy matrix
    """

    user_list = []
    movie_list = []
    rating_list = []
    ratings = RetrieveRating().retrieve_ratings()

    counter = 0
    # Puts everything but every 5th row (1, 2, 3, 4, 6, 7, 8, 9, 11...) in train_matrix
    for rating in ratings:
        if counter % 5 != 0:
            user_list.append(rating.user_id)
            movie_list.append(rating.movie_id)
            rating_list.append(rating.rating)
        counter += 1

    # Added +1 because else the matrix will be to small
    # TODO Change dimensions to greater than 1 if problem with dimensions
    train_matrix = coo_matrix((rating_list, (user_list, movie_list)),
                              shape=(RetrieveUser().retrieve_largest_user_id()+1,
                                     RetrieveMovie().retrieve_largest_movie_id()+1))
    return train_matrix


def get_test_matrix():
    """
    Author: Gustaf Norberg / Alexander Dahl
    Date: 2017-11-06
    Last update: 2017-11-14 by Alexander Dahl
    Purpose:
    returns the test matrix. The matrix is 10% of the user ratings at the moment

    :return: test matrix in the form of a numpy matrix
    """
    test_user_list = []
    test_movie_list = []
    test_rating_list = []

    ratings = RetrieveRating().retrieve_ratings()

    counter = 0
    # Puts every 10th row (5, 15, 25...) in test_matrix
    for rating in ratings:
        if counter % 5 == 0 and counter % 2 == 1:
            test_user_list.append(rating.user_id)
            test_movie_list.append(rating.movie_id)
            test_rating_list.append(rating.rating)
        counter += 1
    # TODO Change dimensions to greater than 1 if problem with dimensions
    test_matrix = coo_matrix((test_rating_list, (test_user_list, test_movie_list)),
                             shape=(RetrieveUser().retrieve_largest_user_id()+1,
                                    RetrieveMovie().retrieve_largest_movie_id()+1))
    return test_matrix


def get_new_users_matrix():
    """
    Author: Gustaf Norberg
    Date: 2017-11-06
    Last update: 2017-11-14 by Alexander Dahl
    Purpose: returns the new users matrix. The matrix is 10 % of the user ratings.
    Is used for showing that model is evolving

    :return: new users matrix in the form of a numpy matrix
    """

    user_list = []
    movie_list = []
    rating_list = []

    ratings = RetrieveRating().retrieve_ratings()

    counter = 0
    # Puts every 10th row (10, 20, 30...) in new_users_matrix
    for rating in ratings:
        if counter % 10 == 0:
            user_list.append(rating.user_id)
            movie_list.append(rating.movie_id)
            rating_list.append(rating.rating)
        counter += 1
    # TODO Change dimensions to greater than 1 if problem with dimensions
    new_users_matrix = coo_matrix((rating_list, (user_list, movie_list)),
                                  shape=(RetrieveUser().retrieve_largest_user_id()+1,
                                         RetrieveMovie().retrieve_largest_movie_id()+1))

    return new_users_matrix


def get_movie_title(movie_id):
    """
    Author: Alexander Dahl
    Date: 2017-11-01
    Last update: 2017-11-13
    Purpose: returns the movie title from a movie id input

    :param movie_id:
    :return: movie name as string
    """
    return RetrieveMovie().retrieve_movie(movie_id).title

"""
This module has the following functions:
Training and saving a lightFM model
Loading a lightFM model
Testing the precision@k for a lightFM model
"""
import os
import pickle
from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from Product.RecommendationManager import gets_from_database as get_matrices


def train_model(filename):
    # TODO When create new user the entire model has to be retrained due to new shape
    """
    Author: Alexander Dahl
    Date: 2017-10-08
    Last update: 2017-10-08
    Purpose: Trains and saves a lightFM model
    :param filename:
    :type filename: string
    """
    # gets the training matrix from the database
    train_matrix = get_matrices.get_train_matrix()

    # Instantiate and train the model
    # epochs is number of iterations of training done on the training matrix.
    model = LightFM(loss='warp')
    model.fit(train_matrix, epochs=20, num_threads=2)
    pickle.dump(model, open(filename, 'wb'))


def load_model(filename):
    """
    Author: Alexander Dahl
    Date: 2017-10-08
    Last update: 2017-11-03
    Purpose: loads trained model
    :param filename:
    :return: lightFM model
    """
    try:
        return pickle.load(open(filename, 'rb'))
    except FileNotFoundError:
        print('Wrong file or file path')


def test_precision(model, matrix, k):
    """
    Author: Alexander Dahl
    Date: 2017-10-08
    Last update: 2017-10-08
    Purpose: returns a test precision for the model at k value.

    :param model: lightFM model
    :param matrix: Matrix from database
    :param k: precision@k
    :return: float
    """
    return precision_at_k(model, matrix, k=k).mean()


def evolve_model(filename, model, new_users_matrix):
    """
    Author: Gustaf Norberg
    Date: 2017-11-09
    Last update: 2017-11-13
    Purpose: evolves the model using fit_partial - an add-on for the already fitted model

    :param model: lightFM model
    :param new_users_matrix: Matrix from database
    :param filename:
    :type filename: string
    """
    model.fit_partial(new_users_matrix, epochs=10)
    pickle.dump(model, open(filename, 'wb'))


def show_evolvement():
    """
    Author: Gustaf Norberg
    Date: 2017-11-09
    Last update: 2017-11-13
    Purpose: Shows, in print, that model evolves after running evolve_model
    """
    print("Generate new model")
    train_model('test_new_model.sav')
    print("Load the new model")
    model = load_model('test_new_model.sav')
    print("Import train matrix (80 % of total user data)")
    print("Import new user data matrix - emulated new user data (10 % of total user data)")
    print(" ")
    train_matrix = get_matrices.get_train_matrix()
    new_users_matrix = get_matrices.get_new_users_matrix()
    k = 10

    print("Check precision @ k for the model based on the train matrix (80 %)")
    precision_before = test_precision(model, train_matrix, k)
    print("Precision before re-training of model")
    print(precision_before)
    print(" ")
    print("Re-train model with the extra users (80 + 10 %)")
    evolve_model('test_new_model.sav', model, new_users_matrix)
    print("Check precision @ k for the model based on the train matrix & new users (90 %)")
    precision_after = test_precision(model, train_matrix + new_users_matrix, k)
    print("Precision after re-training of model")
    print(precision_after)


def get_path():
    """
    Author: Marten Bolin
    Date: 2017-11-30
    Purpose: returns the path to where the model is located.
    :return: string
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path + '/model/new_model.sav'

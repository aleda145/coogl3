"""
creates a plot graph over adadelta and adagrad. Can be used to find out which model parameters
are  best.
"""
import numpy as np
import matplotlib.pyplot as plt
from Product.RecommendationManager.model import generate_model as generate_model


def evolve_model_graph(train_matrix):
    """
    Author: Gustaf Norberg
    Date: 2017-11-15
    Last update: 2017-11-23
    Purpose: Generates a graph to show how quick the model is trained as well as to
    what precision we can train the model. Stops evolving when the change is still bigger than 1 %
    """
    alpha = 1e-3
    # TODO change the constant epochs to be the same as the in generate model
    epochs = 100
    k = 10
    minimum_change = 1 / 100

    adagrad_model = generate_model.LightFM(no_components=30,
                                           loss='warp',
                                           learning_schedule='adagrad',
                                           user_alpha=alpha,
                                           item_alpha=alpha)

    adadelta_model = generate_model.LightFM(no_components=30,
                                            loss='warp',
                                            learning_schedule='adadelta',
                                            user_alpha=alpha,
                                            item_alpha=alpha)

    adagrad_precision_at_k = []
    adadelta_precision_at_k = []
    for i in range(epochs):
        adagrad_model.fit_partial(train_matrix, epochs=1)
        adagrad_precision_at_k.append(generate_model.test_precision(adagrad_model, train_matrix, k))
        adadelta_model.fit_partial(train_matrix, epochs=1)
        adadelta_precision_at_k.append(generate_model.test_precision(adadelta_model, train_matrix,
                                                                     k))
        if (i > 1 and adagrad_precision_at_k[i] - adagrad_precision_at_k[i - 1] < minimum_change and
                adadelta_precision_at_k[i] - adadelta_precision_at_k[i - 1] < minimum_change):
            break

    x_value = np.arange(len(adagrad_precision_at_k))
    plt.plot(x_value, np.array(adagrad_precision_at_k))
    plt.plot(x_value, np.array(adadelta_precision_at_k))
    plt.legend(['adagrad', 'adadelta'], loc='lower right')
    plt.show()

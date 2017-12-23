"""
creating some mock feedback to add to the database
"""
from Product.RecommendationManager.feedback.feedback import Feedback

USER_IDS = [55, 55, 55, 55, 55, 55, 55, 10, 10, 10]
MOVIE_IDS = [1, 2, 5, 4, 2, 4, 3, 6, 4, 8]
WATCHED = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
RATINGS = [5, 4, 3, 2, 1, 3, 4, 5, 2, 1]

for mock in zip(USER_IDS, MOVIE_IDS, WATCHED, RATINGS):
    # instantiates the feedback class to insert feedback
    Feedback().insert_feedback(mock[0], mock[1], mock[2], mock[3])

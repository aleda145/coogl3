"""
    Author: Marten Bolin
    Date: 2017-11-22
    Last update:
    Purpose: This starts the observer that creates and checks
"""

import time
from Product.RecommendationManager.run_recommendation_configurations.recreate_model \
    import RecreateModel
from Product.RecommendationManager.run_recommendation_configurations.update_success_rate \
    import UpdateSuccessRate
from Product.RecommendationManager.Recommendation.create_recommendations_for_all_users \
    import CreateRecommendationsForAllUsers

# Be aware that these will run until terminated! Do not forget them running in the background!
# Instantiate the class that will check for updates and recreate the model
MODEL_UPDATER = RecreateModel()

# Wait for RecreateModel to run once before updating success_rate
time.sleep(2)

# Instantiate the class that will update the succesrate daily
SUCCESS_RATE_UPDATER = UpdateSuccessRate()

STOP_LOOP = False
while not STOP_LOOP:
    try:
        CreateRecommendationsForAllUsers.execute(10)
        STOP_LOOP = True
    except ValueError:
        print("Waiting for TrendScore to commit, wait 5 seconds and then try again")
        time.sleep(5)

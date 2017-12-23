"""
Class for recreating the model.
"""
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from Product.RecommendationManager.model.create_new_model import CreateNewModel
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DatabaseManager.Retrieve.RetrieveRating import RetrieveRating


class RecreateModel:
    """
    Author: Marten Bolin
    Date: 2017-11-22
    Last update:
    Purpose: This will be ran continously to check for any changes made and rearrange the model
    """

    def __init__(self, daemon=False):
        """
        Author: Marten Bolin
        Date: 2017-11-22
        Last update:
        Purpose: The instantiation of the class, make sure to catch it in a variable so it can be
        terminated properly. Start the scheduler
        :param daemon : Sets daemon, (Optional) Default is False
        """
        # Set the variables to start state
        self.number_of_users = 0
        self.number_of_movies = 0
        self.number_of_ratings = 0

        # Set up and start the scheduler
        self.scheduled = BackgroundScheduler()
        if not daemon:
            self.scheduled._daemon = False
        self.scheduled.add_job(self._run, 'interval', seconds=2, id="2")
        self.scheduled.start()
        self.scheduled.modify_job(job_id="2", next_run_time=datetime.now())

    def _run(self):
        """
        Author: Marten Bolin
        Date:2017-11-22
        Last update:
        Purpose: The process that is ran, checks for updates and updates model
        """
        # Get current state
        current_number_of_users = len(RetrieveUser().retrieve_all_users())
        current_number_of_movies = len(RetrieveMovie().retrieve_movie())
        current_number_of_ratings = len(RetrieveRating().retrieve_ratings())
        # Checks rating first due to most likely to change
        if(self.number_of_ratings == current_number_of_ratings and self.number_of_users ==
           current_number_of_users and self.number_of_movies == current_number_of_movies):
            print("Nothing new, no changes made.")
        else:
            print("Changes detected, adjusting model")
            CreateNewModel.create_new_model()
            self.number_of_users = len(RetrieveUser().retrieve_all_users())
            self.number_of_movies = len(RetrieveMovie().retrieve_movie())
            self.number_of_ratings = len(RetrieveRating().retrieve_ratings())

    def terminate(self):
        """
        Author: Marten Bolin
        Date: 2017-11-22
        Last update:
        Purpose: Terminates the process
        """
        print("Shutting down update_recommendations..")
        self.scheduled.shutdown()
        print("Recreatemodel has been shut down.")

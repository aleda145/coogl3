"""
Class for inserting success rate to database
"""
from datetime import datetime
from Product.Database.DatabaseManager.Insert.Insert import Insert
from Product.Database.DBConn import SuccessRate
from Product.Database.DBConn import Recommendation
from Product.Database.DBConn import User
import numpy as np


class InsertSuccessRate(Insert):
    """
    Author: Alexander Dahl, John Andree Lidquist
    Date: 2017-11-22
    Last update: 2017-11-23
    Purpose: Make Insertions of success rate into the database
    """
    def insert_success_rate(self):
        """
        Author: Alexander Dahl, John Andree Lidquist
        Date: 2017-11-22
        Last update: 2017-11-23
        Purpose: Make Insertions of success rate into the database. It calculates the watched,
        not_watched and average_user_experience by querying the database table Recommendation
        and User
        """

        # Calculate watched and not watched up until now.
        # Counts the rows in the Recommendation table that has been watched.
        watched = self.session.query(Recommendation.watched).filter_by(watched=1).count()

        # Counts all the rows minus the ones that are watched
        not_watched = self.session.query(Recommendation).count() - watched

        # Calculate average user success rate up until now for each user
        users = self.session.query(User).all()
        ratio_list = []
        for user in users:
            recommendations = self.session.query(Recommendation).filter_by(user_id=user.id).all()
            num_watched = 0
            num_recommended = 0
            for rec in recommendations:
                num_recommended += 1
                if rec.watched == 1:
                    num_watched += 1
            if num_recommended != 0:
                ratio_list.append(num_watched/num_recommended)

        if watched:
            average_user_success_rate = np.mean(ratio_list).item()
        else:
            average_user_success_rate = 0.0

        # Get todays date
        date_and_time = datetime.now()
        date = date_and_time.date()

        # Make the insertion to the database
        success_rate = SuccessRate(watched=watched,
                                   not_watched=not_watched,
                                   average_user_success_rate=average_user_success_rate,
                                   timestamp=date)
        self.session.add(success_rate)
        self.session.commit()
        self.session.close()

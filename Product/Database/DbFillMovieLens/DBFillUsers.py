"""
Class to fill the database with users
"""
import csv
import os
import sys
from Product.Database.DBConn import User
from Product.Database.DBConn import create_session


class FillUsers:
    """
    Author: Eric Petersson, Vincent Dehaye
    Date: 21-11-2017
    Last update: 21-11-2017
    Purpose: Adds 700 users with mock metadata to the database.
    """
    def __init__(self):
        """
        Author: Eric Petersson, Vincent Dehaye
        Date: 21-11-2017
        Last update: 21-11-2017
        Purpose: Initiates the class and calls the fill method
        """
        self.session = create_session()
        self.fill()

    def fill(self):
        """
        Author: Eric Petersson, Vincent Dehaye
        Date: 21-11-2017
        Last update: 21-11-2017
        Purpose: Adds users by reading csv file with users
        """
        file_path = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file_path += '/MockData/users_with_mock_metadata.csv'
        with open(file_path) as csvfile_users:
            reader = csv.reader(csvfile_users)

            print("Filling database with mock metadata.")
            for line in reader:
                new_user = User(age=int(line[0]), gender=line[1], occupation=line[2])
                self.session.add(new_user)
            self.session.commit()
            self.session.close()
            print("DONE - Users added")

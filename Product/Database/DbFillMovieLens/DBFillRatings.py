"""
Class to fill the database with ratings
"""
import csv
import os.path
from Product.Database.DBConn import create_session
from Product.Database.DBConn import Rating


class FillRatings:
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 12-10-2017
    Last update: 9-11-2017
    Purpose: Fill the database with ratings
    """
    def __init__(self, small_data_set):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 12-10-2017
        Last update: 9-11-2017
        Purpose: Initiate the class and call the fill method
        """
        self.session = create_session()
        self.fill(small_data_set)

    def fill(self, small_data_set):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 12-10-2017
        Last update: 9-11-2017
        Purpose: Read the ratings.csv or smallRatings.csv file and load it into the database.
        :param small_data_set: Boolean that if true will fill the database with the small data set.
        If false it will fill the big data set
        """
        # Columns in the are rating csv files are: userId, movieId, rating, timestamp
        if small_data_set:
            abspath = os.path.dirname(os.path.abspath(__file__)) + '/smallRatings.csv'
            print("Starting to fill ratings from small data set..")

        else:
            abspath = os.path.dirname(os.path.abspath(__file__)) + '/ratings.csv'
            print("Starting to fill ratings from BIG data set..")

        with open(abspath, 'rt') as file:
            reader = csv.reader(file)

            # Iterates through each row in the file
            for row in reader:

                # Iterates through each column
                for counter, column in enumerate(row):

                    if counter == 0:
                        user_id = column

                    if counter == 1:
                        movie_id = column

                    if counter == 2:
                        rating = column
                        new_rating = Rating(movie_id=movie_id, user_id=user_id, rating=rating)
                        self.session.add(new_rating)
                        # There is also a timestamp in the dataset which is not used

        # Commit the added ratings
        self.session.commit()
        self.session.close()
        print("DONE - Ratings added")

        # Close the csv file
        file.close()

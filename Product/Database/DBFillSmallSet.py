"""
Script that will fill the database with the small data set by running DbFillMovieLens files
"""
from Product.Database.DbFillMovieLens.DBFillMovies import FillMovies
from Product.Database.DbFillMovieLens.DBFillRatings import FillRatings
from Product.Database.DbFillMovieLens.DBFillUsers import FillUsers
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser

"""
Author: John Andree Lidquist, Marten Bolin
Date: 2017-10-12
Last update: 2017-11-9
Purpose: Script that will fill the database with the small data set (40 movies) by running
DbFillMovieLens files
"""

# This script will
# 1. Create the a new database (by running DBConn)
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies,
# and DBFillRatings)

# 1. Create the a new database (by running DBConn)
# The import is grayed out, but will run anyway.
import Product.Database.DBConn

retriever = RetrieveUser()
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies
# and DBFillRatings)
if retriever.check_if_user_in_rating(1) is None:
    use_small_set = True
    FillUsers()
    FillMovies(use_small_set)
    FillRatings(use_small_set)
    print("No links added (not necessary)")
    # There are no Links created for the small data set
else:
    print("There is already an existing database.")

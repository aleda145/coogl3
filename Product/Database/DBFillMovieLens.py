"""
Script that will fill the database with the MovieLens data set by running DbFillMovieLens files
"""
from Product.Database.DbFillMovieLens.DBFillMovies import FillMovies
from Product.Database.DbFillMovieLens.DBFillRatings import FillRatings
from Product.Database.DbFillMovieLens.DBFillUsers import FillUsers

"""
Author: John Andree Lidquist, Marten Bolin
Date: 2017-10-12
Last update: 2017-11-9
Purpose: Fills the database with the data set MovieLens
"""

# This script will
# 1. Create the a new database (by running DBConn)
# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies,
# and DBFillRatings)

# 1. Create the a new database (by running DBConn)
# The import is grayed out, but will run anyway.
import Product.Database.DBConn

# 2. Fill it with the data from the data set (by running DBFillUsers, DBFillMovies,
# and DBFillRatings)
use_small_set = False
FillUsers()
FillMovies(use_small_set)
FillRatings(use_small_set)

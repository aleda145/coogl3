"""
Author: Marten Bolin
Date: 2017-10-28
Last update: 2017-11-20
Purpose: Running TrendManager to get trending score for movies in database
"""

import os
from Product.TrendManager.TrendScoreToDatabase import TrendingToDB


# TrendingToDB has two in parameters, daily which sets it to run once daily and daemon which if
# True will make the TrendingToDB to terminate when the application is done
# trending_run.terminate() will stop the TrendingToDB


try:
    RUN_IN_PROD = os.environ['RUN_TREND_CONT'] == '1'
except KeyError:
    RUN_IN_PROD = False
finally:
    if not RUN_IN_PROD:
        TRENDING_RUN = TrendingToDB(daily=False)
    else:
        TRENDING_RUN = TrendingToDB(daily=True)

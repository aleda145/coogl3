"""
Unit tests for TrendScoreToDatabase.py
"""

import time

from Product.TrendManager.TrendScoreToDatabase import TrendingToDB
from Product.Database.DBConn import create_session
from Product.Database.DBConn import TrendingScore


def test_TrendingToDB():
    '''
    Author: John Andree Lidquist, Marten Bolin
    Date: 2017-10-30
    Purpose: Assert that the database gets filled/updated with trending scores.
    '''

    # The test will first start to run the class TrendingToDB
    # and then wait (sleep) for 3 seconds before moving on
    # to make sure that there has been a value stored for
    # the trending score "total_score".
    session = create_session()
    # Pre-conditions
    trend_to_db = TrendingToDB(daily=False)
    time.sleep(3)
    trend_to_db.terminate()
    # Expected output 1
    expected_low = 0

    # Observed output 1
    result = session.query(TrendingScore).filter_by(movie_id=1).first()
    observed = result.total_score
    session.close()
    assert expected_low <= observed

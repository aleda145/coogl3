"""
Test file to test InsertSuccessRate.py
"""
from Product.Database.DatabaseManager.Insert.InsertSuccessRate import InsertSuccessRate
from Product.Database.DBConn import create_session
from Product.Database.DBConn import SuccessRate
import datetime


def test_insert_success_rate():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-28
    Purpose: Assert that success rates are correctly added to the database
    """

    # PRE-CONDITIONS
    # Save the size (the number of rates) before insertion, then make the insertion
    session = create_session()
    rates_before = session.query(SuccessRate).filter_by().all()
    InsertSuccessRate().insert_success_rate()

    # EXPECTED OUTPUT
    expected_size_after = len(rates_before) + 1

    # OBSERVED OUTPUT
    # We query the rates and find the added rate by comparing it to today's date.
    # We also get the size
    rates_after = session.query(SuccessRate).filter_by().all()
    observed_size_after = len(rates_after)

    observed_rate = None
    for rate in rates_after:
        if rate.timestamp.day == datetime.datetime.now().day:
            observed_rate = rate

    session.query(SuccessRate).filter_by(id=observed_rate.id).delete()
    session.commit()
    session.close()

    assert observed_size_after == expected_size_after
    assert observed_rate.watched >= 0
    assert observed_rate.not_watched >= 0
    assert observed_rate.average_user_success_rate >= 0
    assert observed_rate.average_user_success_rate <= 1

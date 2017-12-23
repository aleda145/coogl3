"""
Test file to test SuccessRate.py
"""
from Product.Database.DatabaseManager.Retrieve.RetrieveSuccessRate import RetrieveSuccessRate
from Product.Database.DBConn import create_session
from Product.Database.DBConn import SuccessRate


def test_get_success_rates():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-21
    Last Updated: 2017-11-27
    Purpose: Assert that the success rates are retrieved from the database
    """
    # PRE-CONDITIONS
    watched = 99
    not_watched = 88
    average_user_success_rate = 0.123456789

    # We create a session and add a dummy success rate
    session = create_session()
    dummy_success_rate = SuccessRate(watched=watched, not_watched=not_watched,
                                     average_user_success_rate=average_user_success_rate)
    session.add(dummy_success_rate)
    session.commit()

    # EXPECTED OUTPUT
    expected_watched = watched
    expected_not_watched = not_watched
    expected_user_average_success_rate = average_user_success_rate

    # OBSERVED OUTPUT
    # We call the method to be tested to get all the success rates
    observed = RetrieveSuccessRate().get_success_rates()
    observed_watched = None
    observed_not_watched = None
    observed_average_user_success_rate = None
    # We find the success rate we added
    for rate in observed:
        if rate.average_user_success_rate == average_user_success_rate:
            observed_watched = rate.watched
            observed_not_watched = rate.not_watched
            observed_average_user_success_rate = rate.average_user_success_rate
            break

    # After adding the dummy success rate we remove it.
    session.delete(dummy_success_rate)
    session.commit()
    session.close()

    assert observed
    assert observed_watched == expected_watched
    assert observed_not_watched == expected_not_watched
    assert observed_average_user_success_rate == expected_user_average_success_rate

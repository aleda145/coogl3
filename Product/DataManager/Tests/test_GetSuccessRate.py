"""
Test file to test GetSuccessRate.py
"""
from Product.DataManager.Recommendation.GetSuccessRate import GetSuccessRate
from Product.Database.DBConn import create_session
from Product.Database.DBConn import SuccessRate


def test_get_simple_success_rate():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-27
    Last Updated: 2017-11-27
    Purpose: Assert that the success rates are retrieved from the DataManager correctly
    """
    # PRE-CONDITIONS
    watched = 9999
    not_watched = 8888
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

    # OBSERVED OUTPUT
    # We call the method to be tested to get all the success rates
    observed_dict = GetSuccessRate().get_simple_success_rate()
    observed_watched = None
    observed_not_watched = None
    for entry in observed_dict:
        if entry.get('watched') == expected_watched and \
                        entry.get('not_watched') == expected_not_watched:
            observed_watched = entry.get('watched')
            observed_not_watched = entry.get('not_watched')
            break

    # After adding the dummy success rate, we remove it again
    session.delete(dummy_success_rate)
    session.commit()
    session.close()

    assert len(observed_dict) >= 1
    assert observed_watched == expected_watched
    assert observed_not_watched == expected_not_watched


def test_get_average_user_success_rate():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-27
    Last Updated: 2017-11-27
    Purpose: Assert that the average success rate is retrieved from the DataManager correctly
    """

    # PRE-CONDITIONS
    watched = 9999
    not_watched = 8888
    average_user_success_rate = 0.123456789

    # We create a session and add a dummy success rate
    session = create_session()
    dummy_success_rate = SuccessRate(watched=watched, not_watched=not_watched,
                                     average_user_success_rate=average_user_success_rate)
    session.add(dummy_success_rate)
    session.commit()

    # EXPECTED OUTPUT
    expected_average_user_success_rate = average_user_success_rate

    # OBSERVED OUTPUT
    # We call the method to be tested to get all the success rates
    observed_dict = GetSuccessRate().get_average_user_success_rate()
    observed_average_user_success_rate = None
    for entry in observed_dict:
        if entry.get('average_user_success_rate') == expected_average_user_success_rate:
            observed_average_user_success_rate = entry.get('average_user_success_rate')
            break

    # After adding the dummy success rate, we remove it again
    session.delete(dummy_success_rate)
    session.commit()
    session.close()

    assert len(observed_dict) >= 1
    assert observed_average_user_success_rate == expected_average_user_success_rate

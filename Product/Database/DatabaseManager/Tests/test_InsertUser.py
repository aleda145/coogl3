"""
Test file to test InsertUser.py
"""
from Product.Database.DatabaseManager.Insert.InsertUser import InsertUser
from Product.Database.DBConn import create_session
from Product.Database.DBConn import User


def test_insert_user():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-21
    Last Updated: 2017-11-21
    Purpose: Assert that users are correctly inserted to the database
    """

    # PRE-CONDITIONS
    user_age_1 = 3333
    user_gender_1 = 'Female'
    user_occupation_1 = 'Student'
    user_age_2 = 4444
    user_gender_2 = 'Male'

    # We call the function to be tested and let it add feedback. Two users will be added
    InsertUser().insert_user(user_age_1, user_gender_1, user_occupation_1)
    InsertUser().insert_user(user_age_2, user_gender_2)

    # EXPECTED OUTPUT
    expected_user_age_1 = user_age_1
    expected_user_gender_1 = user_gender_1
    expected_user_occupation_1 = user_occupation_1
    expected_user_age_2 = user_age_2
    expected_user_gender_2 = user_gender_2
    expected_user_occupation_2 = 'Unknown'

    # OBSERVED OUTPUT
    # We query the rating and recommendation to get an observed output
    session = create_session()
    observed_1 = session.query(User).filter(User.age == user_age_1).first()
    observed_user_age_1 = observed_1.age
    observed_user_gender_1 = observed_1.gender
    observed_user_occupation_1 = observed_1.occupation
    observed_2 = session.query(User).filter(User.age == user_age_2).first()
    observed_user_age_2 = observed_2.age
    observed_user_gender_2 = observed_2.gender
    observed_user_occupation_2 = observed_2.occupation

    # After adding the dummy users, we remove them again.
    session.delete(observed_1)
    session.delete(observed_2)
    session.commit()
    session.close()

    assert observed_1
    assert observed_user_age_1 == expected_user_age_1
    assert observed_user_gender_1 == expected_user_gender_1
    assert observed_user_occupation_1 == expected_user_occupation_1
    assert observed_2
    assert observed_user_age_2 == expected_user_age_2
    assert observed_user_gender_2 == expected_user_gender_2
    assert observed_user_occupation_2 == expected_user_occupation_2

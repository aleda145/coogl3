from Product.Database.DBConn import create_session, Recommendation
from Product.DataManager.restrict import get_restricted_match
from Product.RecommendationManager import gets_from_database as gets_from_database

"""
Author: Eric Petersson
Date: 2017-11-15
Last update:
Purpose: Illustrate how restrict.py can be used to generate output for visualization
"""
session = create_session()
# Defines what columns in the User table to restrict on.  Will be a parameter
feature_list = ['gender', 'occupation']

# Defines what is considered a match for gender
matching_strings_list_gender = ['Male', 'Female']

# Defines what is considered a match for occupation
matching_strings_list_occupation = ['engineer', 'student']

# Defines the list, of lists that will be a parameter.
list_of_matching_strings_list = [matching_strings_list_gender, matching_strings_list_occupation]

# Generates the list of users matching the query
list_of_matching_users = get_restricted_match('User', feature_list, list_of_matching_strings_list)

# Will be the list of recommended movies, and the number of time the were recommended.
toplist = {}

# Populates toplist.
for user in list_of_matching_users:
    recommended_to_user = session.query(Recommendation).filter(Recommendation.user_id == user)
    for recommendation in recommended_to_user:
        if recommendation.movie_id not in toplist:
            toplist[recommendation.movie_id] = 1
        else:
            toplist[recommendation.movie_id] += 1

# Prints toplist
for k, v in toplist.items():
    print("Movie: ", gets_from_database.get_movie_title(k), "recommended: ", v, " times")
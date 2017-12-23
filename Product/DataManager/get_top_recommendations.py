from Product.Database.DBConn import create_session, Recommendation
from Product.DataManager.restrict import get_user_group_ids
from Product.RecommendationManager import gets_from_database as gets_from_database

"""
Author: Eric Petersson, Vincent Dehaye
Date: 2017-11-21
Last update: 2017-11-23 Bamse
Purpose: Return the movies which have been the most recommended for the users considered
Parameters:
    nr_of_movies (int): The maximum number of movies that will be returned.
"""

def get_top_recommendations(age_range, gender_list, nr_of_movies):
    # Example call for all users : get_top_recommendations([], [], 10)
    # Example call for only Male and Unknown users : get_top_recommendations([],["Male", "Unknown"])
    # Example call for users only between 15 and 35 : get_top_recommendations([15,35], [])
    # Example call for Female users between 35 and 50 : get_top_recommendations([35,50], ["Female"])

    # Generates the list of users matching the query
    list_of_matching_users = get_user_group_ids(age_range, gender_list)

    # Will be the list of recommended movies, and the number of time the were recommended.
    toplist = {}
    # Count the number of times each movie has been watched
    watched_list  = {}
    session = create_session()

    # Populates top recommended movies list.
    for user in list_of_matching_users:
        recommended_to_user = session.query(Recommendation).filter(Recommendation.user_id == user).all()
        for recommendation in recommended_to_user:
            if recommendation.movie_id not in toplist:
                toplist[recommendation.movie_id] = 1
                if recommendation.watched == 1:
                    watched_list[recommendation.movie_id] = 1
                else:
                    watched_list[recommendation.movie_id] = 0
            else:
                toplist[recommendation.movie_id] += 1
                if recommendation.watched == 1:
                    watched_list[recommendation.movie_id] += 1

    output_list = []

    # Sort the keys of the movies from the most recommended to the least.
    keys = sorted(toplist.items(), key=lambda x: x[1], reverse=True)

    # Fill the list with dictionaries containing movie id, name and count of recommendations
    # in the order of the most recommended to the least.
    for idx in range(min(len(keys), nr_of_movies)):
        tmp_dict = {}
        movie_id, nr_of_recs = keys[idx]
        tmp_dict["id"] = movie_id
        tmp_dict["title"] = gets_from_database.get_movie_title(movie_id)
        tmp_dict["timesRecommended"] = nr_of_recs
        tmp_dict["successRate"] = (watched_list[movie_id]/nr_of_recs)*100
        output_list.append(tmp_dict)

    return output_list

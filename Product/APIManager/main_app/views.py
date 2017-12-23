
"""
Author: Bamse
Date: 2017-09-26
Last update: 2017-11-14 by Bamse
This module contains all the view classes that handle API requests.
"""
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
import traceback
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlalchemy.exc import IntegrityError

from main_app.serializers import RatingSerializer, UserSerializer
from Product.DataManager.Users.InsertNewUser import InsertNewUser
from Product.RecommendationManager.Recommendation.recommendation import Recommendation
from Product.RecommendationManager.feedback.feedback import Feedback
from Product.DataManager.get_top_recommendations import get_top_recommendations
from Product.DataManager.TopTrending.RetrieveTopTrendingTotal import RetrieveTopTrendingTotal
from Product.DataManager.TopTrending.RetrieveTopTrendingTwitter import RetrieveTopTrendingTwitter
from Product.DataManager.TopTrending.RetrieveTopTrendingYoutube import RetrieveTopTrendingYoutube
from Product.DataManager.Recommendation.GetSuccessRate import GetSuccessRate

MINIMUM_AGE = 0
MAXIMUM_AGE = 200
NR_OF_MOVIES_RECOMMENDED = 10

class RecommendationsView(APIView):
    """
    Author: Bamse
    Date: 2017-10-04
    Last update: 2017-11-23 by Bamse
    This class is used to return the top recommendations from Recommendations module
    """

    def get(self, request):
        """
        Author: Bamse
        Date: 2017-11-14
        Last update: 2017-11-23 by Bamse
        Purpose: Handles GET requests to recommendations API. Returns mock data if fetching from
        recommendation doesn't work or if it's empty.
        """
        try:
            age_range = [request.query_params.get("age_lower", MINIMUM_AGE), request
                         .query_params.get("age_upper", MAXIMUM_AGE)]
            gender_list = []
            if request.query_params.get("male", "0") == "1":
                gender_list.append("Male")
            if request.query_params.get("female", "0") == "1":
                gender_list.append("Female")
            if request.query_params.get("other", "0") == "1":
                gender_list.append("Unknown")
            if not gender_list:
                gender_list = ["Male", "Female", "Unknown"]

            nr_of_movies = int(request.query_params.get("number_of_movies",
                                                        NR_OF_MOVIES_RECOMMENDED))

            recommendation_list = get_top_recommendations(age_range, gender_list, nr_of_movies)
            if not recommendation_list:
                recs = {"recommendation_list": [
                    {"title": "Mocked", "id": 1, "timesRecommended": 2, "successRate": 50},
                    {"title": "Horseman", "id": 2, "timesRecommended": 2, "successRate": 50},
                    {"title": "Birdperson", "id": 3, "timesRecommended": 2, "successRate": 50},
                    {"title": "Manman", "id": 4, "timesRecommended": 2, "successRate": 50},
                    {"title": "Cowman", "id": 5, "timesRecommended": 2, "successRate": 50},
                    {"title": "Snakeman", "id": 6, "timesRecommended": 2, "successRate": 50},
                    {"title": "Butterflyman", "id": 7, "timesRecommended": 2, "successRate": 50},
                    {"title": "The extremely ordinary man", "id": 8, "timesRecommended": 2,
                     "successRate": 50},
                    {"title": "Wonderman the movie", "id": 9, "timesRecommended": 2,
                     "successRate": 50},
                    {"title": "Manbat", "id": 10, "timesRecommended": 2, "successRate": 50},
                ]}
            else:
                recs = {"recommendation_list": recommendation_list}

        except ValueError:
            traceback.print_exc()
            recs = {"recommendation_list": [
                {"title": "Mocked", "id": 1, "timesRecommended": 2, "successRate": 50},
                {"title": "Horseman", "id": 2, "timesRecommended": 2, "successRate": 50},
                {"title": "Birdperson", "id": 3, "timesRecommended": 2, "successRate": 50},
                {"title": "Manman", "id": 4, "timesRecommended": 2, "successRate": 50},
                {"title": "Cowman", "id": 5, "timesRecommended": 2, "successRate": 50},
                {"title": "Snakeman", "id": 6, "timesRecommended": 2, "successRate": 50},
                {"title": "Butterflyman", "id": 7, "timesRecommended": 2, "successRate": 50},
                {"title": "The extremely ordinary man", "id": 8, "timesRecommended": 2, "successRate": 50},
                {"title": "Wonderman the movie", "id": 9, "timesRecommended": 2, "successRate": 50},
                {"title": "Manbat", "id": 10, "timesRecommended": 2, "successRate": 50},
            ]}
        except:
            traceback.print_exc()
            recs = {"recommendation_list": [
                {"title": "Mocked", "id": 1, "timesRecommended": 2, "successRate": 50},
                {"title": "Horseman", "id": 2, "timesRecommended": 2, "successRate": 50},
                {"title": "Birdperson", "id": 3, "timesRecommended": 2, "successRate": 50},
                {"title": "Manman", "id": 4, "timesRecommended": 2, "successRate": 50},
                {"title": "Cowman", "id": 5, "timesRecommended": 2, "successRate": 50},
                {"title": "Snakeman", "id": 6, "timesRecommended": 2, "successRate": 50},
                {"title": "Butterflyman", "id": 7, "timesRecommended": 2, "successRate": 50},
                {"title": "The extremely ordinary man", "id": 8, "timesRecommended": 2, "successRate": 50},
                {"title": "Wonderman the movie", "id": 9, "timesRecommended": 2, "successRate": 50},
                {"title": "Manbat", "id": 10, "timesRecommended": 2, "successRate": 50},
            ]}
        return Response(recs)

class UserRecommendationsView(APIView):
    """
    Author: Bamse
    Date: 2017-10-04
    Last update: 2017-11-14 by Bamse
    This class is used to return the top 10 recommendations from Recommendations team
    """
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, user_id):
        """
        Author: Bamse
        Date: 2017-11-14
        Last update: 2017-11-29 by Alexander Dahl
        Purpose: Handles GET requests to recommendations API. Returns mock data if fetching from
        recommendation doesn't work.
        """
        try:
            recs = Recommendation(user_id).generate_recommendation_list().__dict__
        except ValueError:
            traceback.print_exc()
            recs = {"recommendation_list":[
                {"title":"Mocked", "id":1, "score":10},
                {"title":"Mocked", "id":2, "score":10},
                {"title":"Birdperson", "id":3, "score":10},
                {"title":"Manman", "id":4, "score":10},
                {"title":"Cowman", "id":5, "score":10},
                {"title":"Snakeman", "id":6, "score":10},
                {"title":"Butterflyman", "id":7, "score":10},
                {"title":"The extremely ordinary man", "id":8, "score":10},
                {"title":"Wonderman the movie", "id":9, "score":10},
                {"title":"Manbat", "id":10, "score":10},
                ]}
        except IntegrityError:
            return Response("user does not exist.", status=404)
        except:
            traceback.print_exc()
            recs = {"recommendation_list":[
                {"title":"Mocked", "id":1, "score":10},
                {"title":"Mocked", "id":2, "score":10},
                {"title":"Birdperson", "id":3, "score":10},
                {"title":"Manman", "id":4, "score":10},
                {"title":"Cowman", "id":5, "score":10},
                {"title":"Snakeman", "id":6, "score":10},
                {"title":"Butterflyman", "id":7, "score":10},
                {"title":"The extremely ordinary man", "id":8, "score":10},
                {"title":"Wonderman the movie", "id":9, "score":10},
                {"title":"Manbat", "id":10, "score":10},
                ]}
        return Response(recs)

class TrendingView(APIView):

    def get(self, request):
        """
        Author: Bamse
        Date: 2017-11-14
        Last update: 2017-11-14 by Bamse
        Purpose: Handles GET requests to trending API. Returns mock data.
        """
        try:
            trender = RetrieveTopTrendingTotal()
            recs = {"trendingMovies": trender.get_top_trending(10).list()}
            if len(recs["trendingMovies"]) == 0:
                recs = {"trendingMovies":[
                    {"title":"Mocked", "score":1},
                    {"title":"Mocked", "score":2},
                    {"title":"Birdperson", "score":3},
                    {"title":"Manman", "score":4},
                    {"title":"Cowman", "score":5},
                    {"title":"Snakeman", "score":6},
                    {"title":"Butterflyman", "score":7},
                    {"title":"The extremely ordinary man", "score":8},
                    {"title":"Wonderman the movie", "score":9},
                    {"title":"Manbat", "score":10},
                    ]}

        except:
            recs = {"trendingMovies":[
                {"title":"Mocked", "score":1},
                {"title":"Mocked", "score":2},
                {"title":"Birdperson", "score":3},
                {"title":"Manman", "score":4},
                {"title":"Cowman", "score":5},
                {"title":"Snakeman", "score":6},
                {"title":"Butterflyman", "score":7},
                {"title":"The extremely ordinary man", "score":8},
                {"title":"Wonderman the movie", "score":9},
                {"title":"Manbat", "score":10},
                ]}
        return Response(recs)


class YoutubeTrendingView(APIView):

    def get(self, request):
        try:
            trender = RetrieveTopTrendingYoutube()
            recs = {"youtubeMovies": trender.get_top_trending(10).list()}
        except:
            recs = {"youtubeMovies":[
                {"title":"Mocked", "score":1},
                {"title":"Mocked", "score":2},
                {"title":"Birdperson", "score":3},
                {"title":"Manman", "score":4},
                {"title":"Cowman", "score":5},
                {"title":"Snakeman", "score":6},
                {"title":"Butterflyman", "score":7},
                {"title":"The extremely ordinary man", "score":8},
                {"title":"Wonderman the movie", "score":9},
                {"title":"Manbat", "score":10},
                ]}
        return Response(recs)

class TwitterTrendingView(APIView):

    def get(self, request):
        try:
            trender = RetrieveTopTrendingTwitter()
            recs = {"twitterMovies": trender.get_top_trending(10).list()}
        except:
            recs = {"twitterMovies":[
                {"title":"Mocked", "score":1},
                {"title":"Mocked", "score":2},
                {"title":"Birdperson", "score":3},
                {"title":"Manman", "score":4},
                {"title":"Cowman", "score":5},
                {"title":"Snakeman", "score":6},
                {"title":"Butterflyman", "score":7},
                {"title":"The extremely ordinary man", "score":8},
                {"title":"Wonderman the movie", "score":9},
                {"title":"Manbat", "score":10},
                ]}
        return Response(recs)

class FeedbackView(APIView):
    serializer_class = RatingSerializer

    def get(self, request, user_id):
        return UserRecommendationsView().get(request, user_id)

    def post(self, request, user_id):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            try:
                Feedback().insert_feedback(user_id, serializer.validated_data["movie_id"],
                                           serializer.validated_data.get("watched", None),
                                           serializer.validated_data.get("rating", None))
            except ValueError:
                return Response("user or movie does not exist", status=404)
        else:
            return Response(serializer.errors, status=400)
        return Response(serializer.data)

class SuccessRateView(APIView):
    """
    Author: Bamse
    Date: 2017-11-22
    Last update: 2017-11-22 by Bamse
    This class is used to get the success rate from the machine learning algorithm.
    """

    def get(self, request):
        """
        Author: Bamse
        Date: 2017-11-22
        Last update: 2017-11-22 by Bamse
        This function handles GET requests for the success rate from the machine learning algorithm.
        """

        success_rates = {"success_rates":[
            {"title":"Mocked", "id":1, "successRate":10},
            {"title":"Mocked", "id":2, "successRate":9},
            {"title":"Birdperson", "id":3, "successRate":8},
            {"title":"Manman", "id":4, "successRate":8},
            {"title":"Cowman", "id":5, "successRate":7},
            {"title":"Snakeman", "id":6, "successRate":5},
            {"title":"Butterflyman", "id":7, "successRate":4},
            {"title":"The extremely ordinary man", "id":8, "successRate":4},
            {"title":"Wonderman the movie", "id":9, "successRate":3},
            {"title":"Manbat", "id":10, "successRate":2},
            ]}
        return Response(success_rates)
class SimpleSuccessView(APIView):
    def get(self, request):
        # try:
        #     simple_success = {"simpleSuccess": GetSuccessRate.get_simple_success_rate()}
        # except:
        #     traceback.print_exc()
        simple_success = {"simpleSuccess":[
            {"timestamp": "Saturday", "watched": 10, "not_watched": 25},
            {"timestamp": "Sunday", "watched": 20, "not_watched": 30},
            {"timestamp": "Monday", "watched": 22, "not_watched": 40},
            {"timestamp": "Tuesday", "watched": 60, "not_watched": 100},
            {"timestamp": "Wednesday", "watched": 62, "not_watched": 140},
            {"timestamp": "Thursday", "watched": 120, "not_watched": 200},
        ]}
        return Response(simple_success)
class AverageSuccessView(APIView):
    def get(self, request):
        # try:
        #     average_success = {"averageSuccess": GetSuccessRate.get_average_user_success_rate()}
        # except:
        #     traceback.print_exc()
        average_success = {"averageSuccess":[
            {"timestamp": "Saturday", "average_user_success_rate": 20},
            {"timestamp": "Sunday", "average_user_success_rate": 10},
            {"timestamp": "Monday", "average_user_success_rate": 40},
            {"timestamp": "Tuesday", "average_user_success_rate": 35},
            {"timestamp": "Wednesday", "average_user_success_rate": 45},
            {"timestamp": "Thursday", "average_user_success_rate": 88},
        ]}
        return Response(average_success)

class AddUserView(APIView):
    """
    Author: Bamse
    Date: 2017-11-27
    Last update: 2017-11-27 by Bamse
    Purpose: This class allows adding new users to the database
    """
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                InsertNewUser().insert_user(serializer.validated_data["age"],
                                            serializer.validated_data["gender"],
                                            serializer.validated_data["occupation"])
            except:
                traceback.print_exc()
                return Response("unknown error", status=404)
        else:
            return Response(serializer.errors, status=404)
        return Response(serializer.validated_data, status=201)

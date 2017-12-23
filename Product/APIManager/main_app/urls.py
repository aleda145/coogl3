
"""
Author: Bamse
Date: 2017-09-28
Last update: 2017-11-22
Purpose: Mapping URL requests to the API.
"""
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url(r'^api/v1/recommendations/$', views.RecommendationsView.as_view(), name='recommendations'),
    url(r'^api/v1/recommendations/(?P<user_id>[0-9]+)/$', views.UserRecommendationsView.as_view(),
        name='userrecommendations'),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/trending/$', views.TrendingView.as_view(), name='trending'),
    url(r'^api/v1/youtubetrending/$', views.YoutubeTrendingView.as_view(), name='youtubetrending'),
    url(r'^api/v1/twittertrending/$', views.TwitterTrendingView.as_view(), name='twittertrending'),
    url(r'^api/v1/feedback/(?P<user_id>[0-9]+)/$', views.FeedbackView.as_view(), name='feedback'),
    url(r'^api/v1/success-rate/$', views.SuccessRateView.as_view(), name='success-rate-view'),
    url(r'^api/v1/simple-success/$', views.SimpleSuccessView.as_view(), name='simpleSuccess'),
    url(r'^api/v1/average-success/$', views.AverageSuccessView.as_view(), name='averageSuccess'),
    url(r'^api/v1/add-user/$', views.AddUserView.as_view(), name='addUser'),
    url(r'^api/v1/authenticate/', obtain_jwt_token),
]

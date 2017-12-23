"""
Author: Karl Lundvall, Albin Bergvall, Linn Pettersson
Date: 2017-10-12
Purpose: Search module for the YouTube API
"""

import datetime

import pytz as pytz

from googleapiclient.discovery import build

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
# TODO add youtube key here!
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class YoutubeAPI:
    """
    Author: Karl Lundvall, Albin Bergvall, Linn Pettersson
    Date: 2017-10-12
    Purpose: Class responsible for retrieving data from Youtube
    and calculate a trending score based on this data
    """

    def __init__(self):
        self.max_results = 10
        self.category_id = 24
        self.type = "video"
        self.published = 30
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                             developerKey=DEVELOPER_KEY)

    def get_youtube_data(self, keyword):
        """
        Author: Karl Lundvall
        Date: 2017-10-12
        Purpose: Getting the the result from the search with keyword
        :param keyword: keyword, e.g. movie-title
        :return: search response from Youtube API
        """
        search_response = self.youtube.search().list(
            q=keyword,
            part="snippet",
            type=self.type,
            videoCategoryId=self.category_id,
            maxResults=self.max_results,
            publishedAfter=self.get_date(self.published)
        ).execute()
        return search_response

    def get_youtube_score(self, keyword):
        """
        Author: Karl Lundvall, Linn Pettersson
        Date: 2017-11-12
        Purpose: Getting video statistics for the selected videoId´s
        and calculating total trending score
        :param keyword: keyword, e.g. movie-title
        :return: the total trending score for keyword
        """
        keyword = self.add_search_words(keyword)

        search_response = self.youtube.videos().list(
            part="statistics, snippet",
            id=self.get_video_id(keyword)
        ).execute()

        search_results = self.get_total_search_result(keyword)

        total_score = 0

        for video in search_response.get("items", []):
            view_count = self.get_view_count(video)
            like_ratio = self.get_like_count(video)
            publication_date = self.get_publication_date(video)

            score = 1

            if view_count != 0:
                score *= view_count
            if like_ratio != 0:
                score *= like_ratio
            if publication_date != 0:
                score *= publication_date

            # Total score per video
            total_score += score

        # Total score for a keyword search
        total_score *= search_results
        total_score = int(round(total_score))
        if total_score < 0:
            return 0
        return total_score

    @staticmethod
    def add_search_words(keyword):
        """
        Author: Linn Pettersson
        Date: 2017-11-07
        Purpose: Takes the movie title and adds more words to the search of the API
        :param keyword: keyword e.g. movie-title
        :return: new search term
        """
        search_term = keyword + " movie trailer"
        return search_term

    @staticmethod
    def get_view_count(video):
        """
        Author: Karl Lundvall
        Date: 2017-10-12
        Purpose: Getting view count
        :param video: search result from API response
        :return: number of views
        """
        views = video.get("statistics").get("viewCount")
        if views is None:
            return 0
        return int(views)

    @staticmethod
    def get_like_count(video):
        """
        Author: Linn Pettersson
        Date: 2017-11-03
        Purpose: Getting like and dislike count and calculates the ratio
        :param video: search result from API response
        :return: ratio of dislikes/likes
        """
        likes = 0
        get_likes = video.get("statistics").get("likeCount")
        if get_likes is not None:
            likes = int(get_likes)

        dislikes = 0
        get_dislikes = video.get("statistics").get("dislikeCount")
        if get_dislikes is not None:
            dislikes = int(get_dislikes)

        if likes != 0 and dislikes != 0:
            ratio = 1 - (dislikes/likes)
        elif likes != 0:  # If only likes is not equal to 0, the video has 100 % likes
            ratio = 1
        else:
            ratio = 0

        return ratio

    def get_total_search_result(self, keyword):
        """
        Author: Linn Pettersson
        Date: 2017-11-07
        Purpose: Getting the total number of results for a movie search and then
        dividing it by max result (1 000 000) to get a percentage to use in
        trending calculations
        :param keyword: keyword, e.g. movie-title
        :return: totalResult ratio
        """
        total_result = self.get_youtube_data(keyword).get("pageInfo").get("totalResults")

        # Number of total results are divided by the maximum possible number of results
        result_ratio = total_result / 1000000
        return result_ratio

    def get_publication_date(self, video):
        """
        Author: Linn Pettersson
        Date: 2017-11-10
        Purpose: Getting the date when a video was uploaded
        :param video: search result from API response
        :return: number between 0 and 1 were 1 represents a video updated 0 days ago
        """
        curr_date = datetime.datetime.today()

        date = video.get("snippet").get("publishedAt")
        published_at = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")

        days_ago_datetime = curr_date - published_at
        days_ago = int(days_ago_datetime.days)

        # self.published is the variable used in the Youtube API search
        return 1 - (days_ago/self.published)

    def get_video_id(self, keyword):
        """
        Author: Karl Lundvall
        Date: 2017-10-12
        Purpose: Getting the videoId´s from the query
        :param keyword: keyword, e.g. movie-title
        :return: a list containing Youtube video id's
        """
        id_list = ""
        for search_result in self.get_youtube_data(keyword).get("items", []):
            video_id = search_result.get("id").get("videoId")
            if video_id:
                id_list = video_id + ", " + id_list

        return id_list

    @staticmethod
    def get_date(days):
        """
        Author: Karl Lundvall
        Date: 2017-10-12
        Purpose: Getting the date for the inputted number of days ago
        :param days: number of days ago
        :return: date from specified number of days ago
        """
        date = datetime.datetime.utcnow() - datetime.timedelta(days=days)
        date_with_timezone = date.replace(tzinfo=pytz.UTC)
        return date_with_timezone.isoformat()

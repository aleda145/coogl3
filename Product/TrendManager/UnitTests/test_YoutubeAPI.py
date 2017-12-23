"""
Unit tests for YoutubeAPI.py
"""

from ..YoutubeAPI import YoutubeAPI


def test_get_youtube_data_standard_case():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that get_youtube_data returns search results.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = 'Frozen'

    # Expected output
    # > 0

    # Observed output
    observed = youtube.get_youtube_data(keyword)

    assert observed['pageInfo']['totalResults'] > 0


def test_get_youtube_data_bad_input():
    """
    Author: Martin Lundberg
    Date: 2017-10-11
    Purpose: Assert that get_youtube_data doesn't return any results when given gibberish input.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = '!!akjfa asdjk a nganans k a'

    # Expected output
    expected = 0

    # Observed output
    observed = youtube.get_youtube_data(keyword)

    assert observed['pageInfo']['totalResults'] == expected


def test_get_date_standard_case():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that the get_date method in YoutubeAPI returns the correct format.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    days = 30

    # Expected output
    expected = '%Y-%m-%dT%H:%M:%S.%f%z'

    # Observed output
    output = youtube.get_date(days)

    assert output is output.format(expected)


def test_get_date_bad_input():
    """
    Author: Karl Lundvall
    Date: 2017-11-06
    Purpose: Assert that the get_date method in YoutubeAPI does not returns the incorrect format.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    days = 30

    # Expected output
    expected1 = '%Y-%m-%dT%H:%M:%S.%f%z'

    # Bad output
    expected2 = 'Saturday, June 9th, 2007, 5:46:21 PM'

    # Observed output
    output = youtube.get_date(days)

    assert output.format(expected1) is not expected2


def test_get_video_id():
    """
    Author: Karl Lundvall
    Date: 2017-10-09
    Purpose: Assert that get_video_id method in YoutubeAPI returns id´s.
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    # Observed output
    output1 = youtube.get_video_id("IT")
    # Observed output
    output2 = youtube.get_video_id("laskdaslkjdaslkjdaslkdjaslkjdaslkjasdkljadslkdj alkdjaslkjddslak alksdjj")

    assert output1 is not None

    assert output2 is ""


def test_get_youtube_score_standard_case():
    """
    Author: Linn Pettersson
    Date: 2017-10-30
    Purpose: Assert that get_youtube_score calculates
    a total score based on view count and likes ratio
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = 'Thor'

    # Expected output
    # >= 0

    # Observed output
    observed = youtube.get_youtube_score(keyword)

    assert observed >= 0


def test_get_youtube_score_non_existing_keyword():
    """
    Author: Linn Pettersson
    Date: 2017-10-30
    Purpose: Assert that get_youtube_score gets a total score of 0 when the keyword is non existing
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = '2jfklangjdlnf'

    # Expected output
    expected = 0

    # Observed output
    observed = youtube.get_youtube_score(keyword)

    assert observed == expected


def test_get_view_count_standard_case():
    """
    Author: Linn Pettersson
    Date: 2017-10-30
    Purpose: Assert that get_view_count returns the view count for a given keyword
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = 'Thor'

    search_response = youtube.youtube.videos().list(
        part="statistics, snippet",
        id=youtube.get_video_id(keyword)
    ).execute()

    # Expected output
    # >= 0

    # Observed output
    for video in search_response.get("items", []):
        observed = youtube.get_view_count(video)
        assert observed >= 0


def test_get_view_count_non_existing_keyword():
    """
    Author: Linn Pettersson
    Date: 2017-10-30
    Purpose: Assert that get_view_count gets a value of 0 when the keyword is non existing
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = '2jfklangjdlnf'

    search_response = youtube.youtube.videos().list(
        part="statistics, snippet",
        id=youtube.get_video_id(keyword)
    ).execute()

    # Expected output
    expected = 0

    # Observed output
    for video in search_response.get("items", []):
        observed = youtube.get_view_count(video)
        assert observed == expected


def test_get_like_count_standard_case():
    """
    Author: Linn Pettersson
    Date: 2017-10-30
    Purpose: Assert that get_like_count calculates a ratio of dislikes/likes
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = 'Thor'

    search_response = youtube.youtube.videos().list(
        part="statistics, snippet",
        id=youtube.get_video_id(keyword)
    ).execute()

    # Expected output
    # >= 0

    # Observed output
    for video in search_response.get("items", []):
        observed = youtube.get_like_count(video)
        assert observed >= 0


def test_get_like_count_non_existing_keyword():
    """
    Author: Linn Pettersson
    Date: 2017-10-30
    Purpose: Assert that get_like_count gets a ratio of 0 when the keyword is non existing
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = '2jfklangjdlnf'

    search_response = youtube.youtube.videos().list(
        part="statistics, snippet",
        id=youtube.get_video_id(keyword)
    ).execute()

    # Expected output
    expected = 0

    # Observed output
    for video in search_response.get("items", []):
        observed = youtube.get_like_count(video)
        assert observed == expected


def test_add_search_word():
    """
    Author: Linn Pettersson
    Date: 2017-11-08
    Purpose: Assert that multiple words is added to the search keyword
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = "Thor"

    # Expected output
    expected = "Thor movie trailer"

    # Observed output
    observed = youtube.add_search_words(keyword)

    assert observed == expected


def test_get_total_search_result():
    """
    Author: Linn Pettersson
    Date: 2017-11-08
    Purpose: Assert that total search result is fetched and that it calculates a
    result percentage (total hits / max possible hits) and returns a number between 0 and 1
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = "Thor"

    # Expected output
    # >= 0 and <= 1

    # Observed output
    observed = youtube.get_total_search_result(keyword)

    assert (observed >= 0) and (observed <= 1)


def test_get_publication_date():
    """
    Author: Linn Pettersson
    Date: 2017-11-11
    Purpose: Assert that a video get a value between 0 and 1 based on when it has been
    published where 1 eqauls a newly updated video and 0 equals a video updated 30 days ago
    """
    # Pre-conditions
    youtube = YoutubeAPI()
    keyword = "Thor"

    search_response = youtube.youtube.videos().list(
        part="statistics, snippet",
        id=youtube.get_video_id(keyword)
    ).execute()

    # Expected output
    # >= 0 and <= 1

    # Observed output
    for video in search_response.get("items", []):
        observed = youtube.get_publication_date(video)
        assert (observed >= 0) and (observed <= 1)

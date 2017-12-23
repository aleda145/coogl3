"""
Unit tests for TrendingController.py
"""

from ..TrendingController import TrendingController


def test_get_trending_content_standard_case():
    """
    Author: Albin Bergvall, Karl Lundvall
    Date: 2017-11-16
    Purpose: Assert that get_trending_content returns a scored movie
    """
    # Pre-conditions
    trendingcontroller = TrendingController()
    keyword = 'Frozen'

    # Expected output
    # twitter_score > 0
    # youtube_score > 0

    # Observed output
    observed = trendingcontroller.get_trending_content(keyword)

    assert observed.twitter_score > 0
    assert observed.youtube_score > 0


def test_get_trending_content_bad_input():
    """
    Author: Albin Bergvall, Karl Lundvall
    Date: 2017-11-16
    Purpose: Assert that get_trending_content returns
    a scored movie with zero score when given bad input
    """
    # Pre-conditions
    trendingcontroller = TrendingController()
    keyword = 'garga 11 jnargao'

    # Observed output
    observed = trendingcontroller.get_trending_content(keyword)

    assert observed.twitter_score is 0
    assert observed.youtube_score is 0

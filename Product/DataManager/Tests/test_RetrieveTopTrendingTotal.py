from Product.DataManager.TopTrending.RetrieveTopTrendingTotal import RetrieveTopTrendingTotal
from Product.TrendManager.TrendScoreToDatabase import TrendingToDB
import time


def test_get_top_trending():
    """
    Author: John Andrée Lidquist
    Date: 2017-11-13
    Purpose: Assert that movies (titles + total_scores) are returned and that it is the correct amount
    """

    # Pre-conditions
    trender = RetrieveTopTrendingTotal()
    trend_to_db = TrendingToDB(daily=False)
    time.sleep(3)
    trend_to_db.terminate()

    # Expected output
    num_of_movies = 1

    # Observed output
    observed = len(trender.get_top_trending(num_of_movies).list())

    assert observed == num_of_movies

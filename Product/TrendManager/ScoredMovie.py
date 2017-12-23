"""
Author: Albin Bergvall
Date: 2017-11-21
"""


class ScoredMovie:
    """
    Author: Albin Bergvall
    Date: 2017-11-21
    Purpose: Data transfer object class for a scored movie
    """

    def __init__(self):
        """
        Author: Albin Bergvall
        Date: 2017-11-21
        Purpose: Instance variables for the class.
        """
        self.id = None
        self.total_score = 0
        self.youtube_score = 0
        self.twitter_score = 0

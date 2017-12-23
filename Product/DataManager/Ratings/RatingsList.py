class TopTrendingList(object):
    """
    Author: Marten Bolin
    Date: 2017-11-22
    Last update:
    Purpose:
    The list that will be sent to the APIManager
    """
    def __init__(self, list_of_ratings):
        """
        Author: Marten Bolin
        Date: 2017-11-22
        Last update:
        Purpose:
        The constructor of the TopTrendingList, creates a movie list and a score list
        """
        self.list_of_ratings = list_of_ratings

    def print(self):
        """
        Author: Marten Bolin
        Date: 2017-11-22
        Last update:
        Purpose:
        Prints the list
        """
        for rating in self.list_of_ratings:
            print("Rating", rating)

    def list(self):
        """
        Author: Marten Bolin
        Date: 2017-11-22
        Last update:
        Purpose:
        Returns the list as a list of dict
        """
        result = []
        for ratings in zip(self.list_of_ratings):
            result.append({"rating": ratings})
        return result

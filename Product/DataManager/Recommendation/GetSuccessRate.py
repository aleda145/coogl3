"""
Retrieves two different Success Rate from the database
"""
from Product.Database.DatabaseManager.Retrieve.RetrieveSuccessRate import RetrieveSuccessRate


class GetSuccessRate:
    """
    Author: John Andree Lidquist, David Cerny
    Date: 2017-11-20
    Last update: 2017-11-23
    Purpose: Retrieves two different Success Rate from the database
    """

    @staticmethod
    def get_simple_success_rate():
        """
        Author: John Andree Lidquist, David Cerny
        Date: 2017-11-20
        Last update: 2017-11-23
        Purpose: Retrieve the values watched, not_watched and the timestamp from the table
        SuccessRate from the database and returns them in a list of dictionaries.
        :return List of dictionaries with keys watched, not_watched and timestamp
        """
        success_rate_dict = []
        all_rates = RetrieveSuccessRate().get_success_rates()
        for rate in all_rates:
            success_rate_dict.append({'watched': rate.watched, 'not_watched': rate.not_watched,
                                      'timestamp': rate.timestamp})
        return success_rate_dict

    @staticmethod
    def get_average_user_success_rate():
        """
        Author: John Andree Lidquist, David Cerny
        Date: 2017-11-20
        Last update: 2017-11-23
        Purpose: Retrieve the value average_user_success_rate and timestamp from the table
        SuccessRate from the database and returns them in a list of dictionaries.
        :return List of dictionaries with keys average_user_success_rate and timestamp
        """

        result = []
        all_rates = RetrieveSuccessRate().get_success_rates()
        for rate in all_rates:
            result.append({'average_user_success_rate': rate.average_user_success_rate,
                           'timestamp': rate.timestamp})
        return result

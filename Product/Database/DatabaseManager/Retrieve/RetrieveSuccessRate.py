"""
Class for retrieving success rates from database
"""
from Product.Database.DatabaseManager.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import SuccessRate


class RetrieveSuccessRate(Retrieve):
    """
    Author: John Andree Lidquist, David Cerny
    Date: 2017-11-20
    Last update: 2017-11-23
    Purpose: Retrieve data from the success rate table in the database
    """
    def get_success_rates(self):
        """
        Author: John Andree Lidquist, David Cerny
        Date: 2017-11-20
        Last update: 2017-11-23
        Purpose: Retrieve data from the success rate table in the database
        :return The list of all the successrate entries in the database
        """
        return self.session.query(SuccessRate).all()


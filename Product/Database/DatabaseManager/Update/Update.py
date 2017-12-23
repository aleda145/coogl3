"""
The Update super class
"""
from Product.Database.DBConn import create_session


class Update:
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 9/11/2017
    Last update: 13/11/2017
    Purpose: Its subclasses should be used to retrieve from the database
    """
    def __init__(self):
        """
        Author: Marten Bolin, John Lidquist
        Date: 2017-11-10
        Last update:
        Purpose:
        The constructor of the Retrieve class, creates a session to be used by subclass
        """
        self.session = create_session()

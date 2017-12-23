"""
The Insert super class
"""
from Product.Database.DBConn import create_session


class Insert:
    """
    Author: Marten Bolin / John Lidquist
    Date: 2017-11-10
    Last update:
    Purpose:
    Its subclasses should be used to insert to the database
    """
    def __init__(self):
        """
        Author: Marten Bolin / John Lidquist
        Date: 2017-11-10
        Last update:
        Purpose:
        The constructor of the Insert class, creates a session to be used by subclasses
        """
        self.session = create_session()

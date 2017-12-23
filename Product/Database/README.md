Authour: John Andrée Lidquist (johli715)
TODO: add part about DBFillTrending and DBFillVizualization

In this README the structure of the database folder and its content is further explained:

Structure of Database:
In the Database folder, there are currently 2 folders: "DbFillMovieLens" and "Tests". There are also some important files: "DBConn.py", "DBFillMovieLens", "app.db"

- DbFillMovieLens Folder:
    In the DbFillMovieLens folder there are 4 python files that each will fill the database with some content (Users, Links, Movies or Ratings).
    Each of these use a csv file with the raw data, and adds it to the database.
- Tests Folder:
    In the Tests Folder, a unit test has been created: test_DBFillFunctions. This unit test will test to see that the right data has been added to the database after the database has been created and filled.

- DBConn.py
    This file is the one needed to be run in order to create the database. It holds the information about sql table is modeled.
- DBFillMovieLens.py
    This file can be run after creating the database. It is a simple script to run the four DBFill files in the DBFillMovieLens, so that you don't have to run them all seperately.
- app.db
    This is the actual database file with all the data. If you do not have it, look how to create it below.

How to add the database:

- If you create and add all the data straight away, do the following:
    STEP - ACTION
    1 - If you already have the database and want to recreate it - delete the file "app.db". If you don't have it, begin at step 2
    2 - Run DBConn.py
    3 - Run DBFillMovieLens.py

- If you want to just create the database and add the just specific data, do the following
    STEP - ACTION
    1 - If you already have the database and want to recreate it - delete the file "app.db". If you don't have it, begin at step 2
    2 - Run DBConn.py
    3 - Choose and run one of the four DBFill files of your choice in the DbFillMovieLens folder to fill that specific data.

"""
Class to fill the database with movies
"""
import csv
import re
import os
from Product.Database.DBConn import create_session, Movie, MovieInGenre, Genre


class FillMovies:
    """
    Author: John Andree Lidquist, Marten Bolin
    Date: 12-10-2017
    Last update: 9-11-2017
    Purpose: Read the movie_id.csv/smallMovies.csv file and load it into the database.
    Columns in the are movie csv files: userId, movieId, rating, timestamp
    """
    def __init__(self, small_data_set):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 12-10-2017
        Last update: 9-11-2017
        Purpose: Initiate the class and call the fill method
        """
        self.session = create_session()
        self.fill(small_data_set)

    def fill(self, small_data_set):
        """
        Author: John Andree Lidquist, Marten Bolin
        Date: 12-10-2017
        Last update: 9-11-2017
        Purpose: Load the different genres and movies in movies.csv file into the database.
        """
        # This part handles adding the different genres to the databas
        # List of all genres that can be se en in the movie lens dataset
        genres = ["Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
                  "Drama", "Fantasy", "Film-Noir", "Horror", "IMAX", "Musical", "Mystery",
                  "Romance", "Sci-Fi", "Thriller", "War", "Western", "(no genres listed)"]

        # Add the genres to the db
        for genre in genres:
            new_genre = Genre(name=genre)
            self.session.add(new_genre)

        # This part handles adding the movies of the dataset into the database
        # Read the movie.csv file to add data into database
        # Columns in the ratings.csv: movieID, titleAndYear, Genres
        if small_data_set:
            abspath = os.path.dirname(os.path.abspath(__file__)) + '/smallMovies.csv'
            print("Starting to fill movies from small data set..")
        else:
            abspath = os.path.dirname(os.path.abspath(__file__)) + '/movies.csv'
            print("Starting to fill movies from BIG data set..")

        with open(abspath, 'rt', encoding="utf-8") as file:
            reader = csv.reader(file)
            # Iterates through each row in the file and take column one (id) and column 2 (title)
            for row in reader:
                # Search the title string of row[1] of occurances for (yyyy) and (yyyy-) for series
                # Then checks length if it was found and puts it in the new_movie if year is
                # not found it goes into the else statement and no year is inputted to the creation
                search_for_year = re.split(r" \(([0-9][0-9][0-9][0-9])+\)", row[1])
                search_for_year_series = re.split(r"\(([0-9][0-9][0-9][0-9]-)+\)", row[1])
                if len(search_for_year) > 1:
                    new_movie = Movie(id=row[0], title=search_for_year[0], year=search_for_year[1])
                elif len(search_for_year_series) > 1:
                    new_movie = Movie(id=row[0], title=search_for_year_series[0],
                                      year=search_for_year_series[1])
                else:
                    new_movie = Movie(id=row[0], title=row[1])
                self.session.add(new_movie)

            # Need to commit before filling with movies-genre due to foreign key
            self.session.commit()
            file.close()

        with open(abspath, 'rt', encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                for counter, column in enumerate(row):
                    if counter == 0:
                        movie_id = column

                    if counter == 2:
                        genres = column.split("|")

                        # loop through all genres for the movie
                        for new_genre in genres:
                            new_movie_genre = MovieInGenre(movie_id=movie_id, genre=new_genre)
                            self.session.add(new_movie_genre)

        # Commit the added link between movies and their genres
        self.session.commit()
        self.session.close()
        print("DONE - Movies added")

        # Close the csv file
        file.close()

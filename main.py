from csv import DictReader
from movie import Movie
from fresh_tomatoes import open_movies_page

# create movies list
movies = []
with open('movies.csv') as csvfile:
    # read csv file as dict
    reader = DictReader(csvfile)
    # iterate through each row
    for row in reader:
        # create a movie and append it to movies list
        movies.append(Movie(row['title'],
                            row['synopsis'],
                            row['poster'],
                            row['trailer']))
# open the movies page
open_movies_page(movies)

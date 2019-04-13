#import statements
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from SI507project_tools import Base, Movie, Actor, Genre
import csv

###

engine = create_engine('sqlite:///movie_sources.sqlite')
Base.metadata.bind = engine

### initialize session

DBSession = sessionmaker(bind=engine)
session = DBSession()

### open csv
CSV_FILE  = 'wiki_movie_plots_deduped.csv'

movies_data = []

# open csv file
with open(CSV_FILE, newline='') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        movies_data.append(row)


# helper functions

### insert records

## for movies

# for item in movies_data[1:]:
#     new_movie = Movie(
#     ReleaseYear = item[0],
#     Title = item[1],
#     Origin = item[2],
#     Director = item[3],
#     WikiPage = item[6],
#     Plot = item[7]
#     )
#
#     session.add(new_movie)
#
# session.commit()

## for genre

# genre index
possible_genres = ['action','adventure','comedy','crime','drama','fantasy','historical','horror','mystery','thriller','documentary','romance','parody','sci-fi','western','musical','family','animation']

# add genre to database
genres_insert = []

movie_ref = session.query(Movie).all()
movie_dict = {}

for item in movie_ref:
    if item.Title not in movie_dict:
        movie_dict[item.Title] = item.Id
    else:
        pass

for item in movies_data[1:]:
    genre_holder = []
    # identify split
    if '/' in item[5]:
        genre_holder = item[5].split('/')
    elif ',' in item[5]:
        genre_holder = item.[5].split(',')
    else:
        genre_holder = item[5].split()
    # remove spaces
    genre_holder2 = ''
    for item[0] in genre_holder:
        genre_holder2 = item[0].rstrip()
    #check in genre_dictionary
    if genre_holder2 in possible_genres:





## for actor

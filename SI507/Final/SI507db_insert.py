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

# helper definitions
possible_genres = ['action','adventure','comedy','crime','drama','fantasy','historical','horror','mystery','thriller','documentary','romance','parody','sci-fi','western','musical','family','animation','other']

# helper functions

def standardize_genre(movie_obj):
    genre_holder = []
    # identify split
    if '/' in movie_obj[5]:
        genre_holder = movie_obj[5].split('/')
    elif ',' in movie_obj[5]:
        genre_holder = movie_obj[5].split(',')
    else:
        genre_holder = movie_obj[5].split()
    # take first genre mentioned, and compare to possible_genres
    try:
        genre_ref = genre_holder[0].lstrip()
        if genre_ref.lower() in possible_genres:
            movies_genre = genre_ref.lower()
        else:
            movies_genre = 'other'
    except:
        movies_genre = 'n/a'
    return movies_genre

def check_genre(genre_name):
    genre = session.query(Genre).filter_by(Name=genre_name).first()
    if genre:
        return genre
    else:
        genre = Genre(Name=genre_name)
        session.add(genre)
        session.commit()
        return genre

### insert records

## for movies

for item in movies_data[1:]:
    genre = check_genre(standardize_genre(item))

    new_movie = Movie(
    ReleaseYear = item[0],
    Title = item[1],
    Origin = item[2],
    Director = item[3],
    WikiPage = item[6],
    Plot = item[7],
    GenreName = genre.Name
    )

    session.add(new_movie)

session.commit()


## for actor

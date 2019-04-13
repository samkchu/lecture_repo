# Import statements
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

### DATABASE MODEL

# create base
Base = declarative_base()

# create model
association_table = Table('association', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.Id')),
    Column('right_id', Integer, ForeignKey('actors.Id')))

class Movie(Base):
    __tablename__ = 'movies'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    ReleaseYear = Column(Integer)
    Title = Column(String(100))
    Origin  = Column(String(100))
    Director = Column(String(100))
    WikiPage = Column(String(100))
    Plot = Column(String(5000))
    Genre_Id = Column(Integer,ForeignKey('genres.Id'))
    Genre = relationship('Genre',backref='movies')
    Actors = relationship('Actor',secondary=association_table,backref='movies')

class Genre(Base):
    __tablename__ = 'genres'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    GenreName = Column(String(100))

class Actor(Base):
    __tablename__ = 'actors'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    ActorFirstName = Column(String(100))
    ActorLastName = Column(String(100))

# Create engine

engine = create_engine('sqlite:///movie_sources.sqlite', echo=False)

# Create tables in engine

Base.metadata.create_all(engine)

### PLOT GENERATOR FUNCTIONS

### PLOTLY FUNCTIONS

### IFMAIN STATEMENT

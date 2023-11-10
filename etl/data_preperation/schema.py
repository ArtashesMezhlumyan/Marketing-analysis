
# from ..logger import CustomFormatter

import logging
import os

import logging
from ..logger import CustomFormatter

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


from sqlalchemy import create_engine,Column,Integer,String,Float, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

engine=create_engine('sqlite:///temp.db')

Base= declarative_base()

# Define the RatingsSmall table
class Rating(Base):
    __tablename__ = "Ratings_small"

    user_id = Column(Integer, ForeignKey('User.user_id'), primary_key=True)
    movie_id = Column(Integer, ForeignKey('MovieMetadata.movie_id'), primary_key=True)
    rating = Column(Float)

# Define the MovieMetadata table
class MovieMetadata(Base):
    __tablename__ = "MovieMetadata"

    movie_id = Column(Integer, primary_key=True)
    title = Column(String)
    budget = Column(Float)
    revenue = Column(Float)
    release_date = Column(Date)
    language = Column(String)
    production_country = Column(String)
    production_company = Column(String)

    credits = relationship("Credits", back_populates="movie")
    keywords = relationship("Keywords", back_populates="movie")
    links_small = relationship("LinksSmall", back_populates="movie")

# Define the Credits table
class Credits(Base):
    __tablename__ = "Credits"

    movie_id = Column(Integer, ForeignKey('MovieMetadata.movie_id'), primary_key=True)
    cast = Column(String)  # Assuming cast is a string field
    crew = Column(String)  # Assuming crew is a string field

    movie = relationship("MovieMetadata", back_populates="credits")

# Define the Keywords table
class Keywords(Base):
    __tablename__ = "plot_keywords"

    movie_id = Column(Integer, ForeignKey('MovieMetadata.movie_id'), primary_key=True)
    plot_keywords = Column(String)
    movie = relationship("MovieMetadata", back_populates="keywords")

class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    age = Column(Integer)
    
    # Define other user-related attributes here

    ratings = relationship("RatingsSmall")

Base.metadata.create_all(engine)

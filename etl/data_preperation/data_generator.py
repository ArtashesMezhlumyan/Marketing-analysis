from faker import Faker
import pandas as pd
import random
import logging
from ..logger import CustomFormatter
import os
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

fake=Faker()



# Data Models

## movie data
def generate_movie_metadata(movie_id):
    return {
        "movie_id": movie_id,
        "title": fake.catch_phrase(),
        "budget": round(random.uniform(1000000, 100000000), 2),
        "revenue": round(random.uniform(1000000, 1000000000), 2),
        "release_date": fake.date_between(start_date="-30y", end_date="today").strftime("%Y-%m-%d"),
        "language": fake.language_code(),
        "production_country": fake.country(),
        "production_company": fake.company()
    }

## user generator
def generate_user(user_id):
    return {
        "user_id": user_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": fake.random_int(min=18, max=70),
        # Add other attributes relevant to a user here
    }


##rating

def generate_ratings(user_id, movie_id):
    rating = round(random.uniform(1.0, 5.0), 2)
    return {
        "user_id": user_id,
        "movie_id": movie_id,
        "rating": rating
    }

#credits

def generate_credits(movie_id):
   
    return  {
        "movie_id": movie_id,
        "cast": [fake.name() for _ in range(random.randint(5, 15))],
        "crew": [fake.name() for _ in range(random.randint(5, 15))]
    }

##keywords

def generate_keywords(movie_id):
    plot_keywords = ", ".join([fake.word() for _ in range(random.randint(3, 10))])

    return {
        "movie_id": movie_id,
        "plot_keywords": plot_keywords
    }




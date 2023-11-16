
# Inside movie_recommender/__init__.py

# Import the preview function from the database module
from .database import preview

# If you have a class or other functions in recommender.py that you want to make available:
from .recommender import MovieRecommender  # Assuming you have a class named MovieRecommender

# You can also import any other necessary functions or classes here
from etl.movie_recommender.recommender import MovieRecommender
from etl.movie_recommender.database import preview

# Function to get recommendations for a given movie title
def get_recommendations_for_movie(movie_title, num_recommendations=10):
    # Load movie data
    movie_data = preview('MovieMetadata')  # Ensure this function returns a DataFrame

    # Create an instance of the recommender
    recommender = MovieRecommender(movie_data)

    # Get recommendations for the chosen movie
    recommendations = recommender.recommend_movies(movie_title, num_recommendations=num_recommendations)
    
    input_movie_id = movie_data[movie_data['title'] == movie_title]['movie_id'].iloc[0]
    recommended = recommendations.tolist()

    # Return the recommendations
    return   [input_movie_id, movie_title, recommended]

# Set the movie title
test_movie_title = "Polarized zero tolerance strategy"

# Get and print recommendations
recommendations = get_recommendations_for_movie(test_movie_title)
print(f"Recommendations for '{test_movie_title}':")
print(recommendations)

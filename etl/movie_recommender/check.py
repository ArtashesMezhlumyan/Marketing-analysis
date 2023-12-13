from .recommender import MovieRecommender
from .database import preview

# Function to get recommendations for a given movie title
def get_recommendations_for_movie(movie_title, num_recommendations=10):
    # Load movie data
    movie_data = preview('MovieMetadata')  # Ensure this function returns a DataFrame

    # Create an instance of the recommender
    recommender = MovieRecommender(movie_data)

    # Get recommendations for the chosen movie
    recommended_titles = recommender.recommend_movies(movie_title, num_recommendations=num_recommendations)

    # Create a list to store recommended movie ids and titles
    recommendations_with_ids = []

    # Retrieve the movie ID for each recommended movie and add it to the recommendations list
    for title in recommended_titles:
        # Assuming the movie_data DataFrame is indexed by movie titles for efficient lookup
        movie_id = movie_data.loc[movie_data['title'] == title, 'movie_id'].iloc[0]
        recommendations_with_ids.append(f"{movie_id}, {title}")

    # Return the formatted recommendations
    return recommendations_with_ids

# # Usage
# test_movie_title = "Organized mission-critical core"
# recommendations = get_recommendations_for_movie(test_movie_title)

# # Print recommendations
# print(f"Recommendations for '{test_movie_title}':")
# for recommendation in recommendations:
#     print(recommendation)

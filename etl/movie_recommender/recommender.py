
# from .database import preview

# movie_data = preview('MovieMetadata')

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class MovieRecommender:
    def __init__(self, movie_data):
        self.movie_data = movie_data
        self.movie_data['title'] = self.movie_data['title'].fillna('')  # Fill NA values
        self.tfidf_matrix = self.create_tfidf_matrix()
        self.similarity_matrix = self.calculate_similarity()

    def create_tfidf_matrix(self):
        # Assuming that you want to calculate similarity based on the movie titles
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.movie_data['title'])
        return tfidf_matrix

    def calculate_similarity(self):
        # Compute the cosine similarity matrix
        cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        return cosine_sim

    def recommend_movies(self, movie_title, num_recommendations=10):
        # Get the index of the movie that matches the title
        indices = pd.Series(self.movie_data.index, index=self.movie_data['title']).drop_duplicates()
        idx = indices[movie_title]

        # Get the pairwise similarity scores of all movies with that movie
        sim_scores = list(enumerate(self.similarity_matrix[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:num_recommendations+1]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar movies
        return list(self.movie_data['title'].iloc[movie_indices])
    
    def get_movie_id(self, movie_title):
        # Get the index of the movie that matches the title
        indices = pd.Series(self.movie_data.index, index=self.movie_data['title']).drop_duplicates()
        movie_id = indices.get(movie_title)
        
        return movie_id


# movie_data = preview('MovieMetadata')
# #print(movie_data)
# recommender = MovieRecommender(movie_data)
# recommendations = recommender.recommend_movies('Polarized zero tolerance strategy', num_recommendations=10)
# print(recommendations)

# recommender = MovieRecommender(movie_data)
# movie_id = recommender.get_movie_id('Polarized zero tolerance strategy')
# print(f"ID of 'Polarized zero tolerance strategy': {movie_id}")
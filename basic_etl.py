
from etl.data_preperation import SqlHandler
from etl.logger import CustomFormatter
import pandas as pd

from etl.data_preperation import SqlHandler
from etl.logger import CustomFormatter
import pandas as pd

# # Create SQL handlers for each table

Inst_movie_metadata = SqlHandler('temp', 'MovieMetadata')
Inst_user = SqlHandler('temp', 'User')
Inst_ratings_small = SqlHandler('temp', 'Ratings_small')
Inst_credits = SqlHandler('temp', 'Credits')
Inst_keywords = SqlHandler('temp', 'plot_keywords')


# # Load data from respective CSV files
movie_data = pd.read_csv('movie_metadata.csv')
user_data = pd.read_csv('users.csv')
ratings_data = pd.read_csv('ratings.csv')
credits_data = pd.read_csv('credits_data.csv')
keywords_data = pd.read_csv('keywords.csv')

# # Insert data into respective SQL tables
Inst_movie_metadata.insert_many(movie_data)
Inst_user.insert_many(user_data)
Inst_ratings_small.insert_many(ratings_data)
Inst_credits.insert_many(credits_data)
Inst_keywords.insert_many(keywords_data)

# # Close connections for each table
Inst_movie_metadata.close_cnxn()
Inst_user.close_cnxn()
Inst_ratings_small.close_cnxn()
Inst_credits.close_cnxn()
Inst_keywords.close_cnxn()
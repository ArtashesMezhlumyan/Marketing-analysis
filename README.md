# ETL with Python


With `__init__.py` files we have managed make our modules accessible. Likewise the `setup.py`

In data preperation directory we have:

- `data_generator.py:` for simulating movie data by using `faker` package
- `schema.py:` for desinging the schema according to our dataset
- `sql_interactions.py:` building dynamic, reproducible **CRUD** operations
- `recommender.py:` This file contains the core recommendation algorithm. It uses cosine distance to evaluate the similarity between movies.
- `check.py:` This script runs the recommendation algorithm implemented in recommender.py and returns the top 10 movie recommendations along with their IDs.
- `run.py:` Run this script to launch the API. It opens a new window where you can modify the movie dataset (insert or delete entries) and obtain recommendations. The recommendations and movie data are stored in a database for persistent access.

  
## How to Run the code

# Step 1


Run `schema_builder.py` which will create  `temp.db` file in your folder.

# Step 2

Run `basic_etl.py` file, you will see all the needed data. 

This file Initializes SQL handlers for different tables like MovieMetadata, User, Ratings_small, Credits, and plot_keywords.
Facilitates the transfer of data from CSV files into an SQL database 

# Step 3 

To get movie recommendations:

Run python check.py.
This will output the top 10 recommended movies based on the current dataset.

# Step 4 

To use the API:

Run python run.py.
A new window will open for dataset modifications and to fetch recommendations.

## Data description

movies_metadata.csv: The main Movies Metadata file. Contains information on movies. Features include posters, backdrops, budget, revenue, release dates, languages, production countries and companies.

keywords.csv: Contains the movie plot keywords for our MovieLens movies. 

credits.csv: Consists of Cast and Crew Information for all our movies. 

rating.csv: The subset of  ratings from  users on  movies.

## MK Docks

Link to our MK Docks: https://petopet7.github.io/MK_Docs-1/

## Example Of Uage
You can find example.ipynb and example.slides.html files in our github which shows how you can useour package.


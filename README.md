# ETL with Python


With `__init__.py` files we have managed make our modules accessible. Likewise the `setup.py`

In data preperation directory we have:

- `data_generator.py:` for simulating movie data by using `faker` package
- `schema.py:` for desinging the schema according to our dataset
- `sql_interactions.py:` building dynamic, reproducible **CRUD** operations


## How to Run the code

# Step 1

.
Run `schema_builder.py` which will create  `temp.db` file in your folder.

# Step 2

Run `basic_etl.py` file, you will see all the needed data. 

This file Initializes SQL handlers for different tables like MovieMetadata, User, Ratings_small, Credits, and plot_keywords.
Facilitates the transfer of data from CSV files into an SQL database 

## Data description

movies_metadata.csv: The main Movies Metadata file. Contains information on movies. Features include posters, backdrops, budget, revenue, release dates, languages, production countries and companies.

keywords.csv: Contains the movie plot keywords for our MovieLens movies. 

credits.csv: Consists of Cast and Crew Information for all our movies. 

rating.csv: The subset of  ratings from  users on  movies.

## MK Docks

Link to our MK Docks: https://petopet7.github.io/MK_Docs-1/


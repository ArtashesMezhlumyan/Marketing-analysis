

import sqlite3
import pandas as pd

def preview(table):
    # Open a connection to the database file
    conn = sqlite3.connect('temp.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Execute a SQL query to select data from the table
    cursor.execute(f"SELECT * FROM {table}")

    # Fetch all the data from the executed query
    data = cursor.fetchall()

    # Get column names from the cursor description
    column_names = [desc[0] for desc in cursor.description]

    # Create a DataFrame from the data and assign column names
    df = pd.DataFrame(data, columns=column_names)

    # Print the DataFrame
    print(df)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    return df
print(preview("MovieMetadata"))
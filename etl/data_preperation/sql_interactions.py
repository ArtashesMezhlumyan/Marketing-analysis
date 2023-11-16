import sqlite3
import logging 
import pandas as pd
import numpy as np
import os
from ..logger import CustomFormatter

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

class SqlHandler:
    """
    A class to handle common SQL operations using sqlite3.

    Attributes
    ----------
    dbname : str
        The name of the database.
    table_name : str
        The name of the table to perform operations on.
    cnxn : sqlite3.Connection
        The SQLite database connection object.
    cursor : sqlite3.Cursor
        The cursor object for the database.

    Methods
    -------
    close_cnxn()
        Closes the database connection.
    get_table_columns()
        Retrieves the column names from the table.
    truncate_table()
        Deletes all records from the table.
    drop_table()
        Drops the table from the database.
    insert_many(df)
        Inserts multiple records from a DataFrame into the database table.
    from_sql_to_pandas(chunksize, id_value)
        Loads data from the SQL table into a pandas DataFrame in chunks.
    update_table(condition)
        Updates records in the table based on a condition.
    """
    def __init__(self, dbname:str,table_name:str) -> None:
        """
        Constructs all the necessary attributes for the SqlHandler object.

        Parameters
        ----------
        dbname : str
            The name of the database file without the extension.
        table_name : str
            The name of the table to perform operations on.
        """
        self.cnxn=sqlite3.connect(f'{dbname}.db')
        self.cursor=self.cnxn.cursor()
        self.dbname=dbname
        self.table_name=table_name

    def close_cnxn(self)->None:
        """
        Commits changes and closes the database connection.
        """

        logger.info('commiting the changes')
        self.cursor.close()
        self.cnxn.close()
        logger.info('the connection has been closed')

    def insert_one(self, data_to_insert: dict) -> None:
        """
        Inserts a single record into the table.

        Parameters
        ----------
        data_to_insert : dict
            A dictionary where keys are column names and values are the corresponding data to insert.
        """
        columns = ', '.join(data_to_insert.keys())
        placeholders = ', '.join(['?'] * len(data_to_insert))
        values = tuple(data_to_insert.values())

        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.cnxn.commit()
        logger.info('One record inserted successfully.')
        

    def get_table_columns(self)->list:
        self.cursor.execute(f"PRAGMA table_info({self.table_name});")
        columns = self.cursor.fetchall()
        
        column_names = [col[1] for col in columns]
        logger.info(f'the list of columns: {column_names}')
        # self.cursor.close()

        return column_names
    
    def truncate_table(self)->None:
        
        query=f"DROP TABLE IF EXISTS {self.table_name};"
        self.cursor.execute(query)
        logging.info(f'the {self.table_name} is truncated')
        # self.cursor.close()

    def drop_table(self):
        
        query = f"DROP TABLE IF EXISTS {self.table_name};"
        logging.info(query)

        self.cursor.execute(query)

        self.cnxn.commit()

        logging.info(f"table '{self.table_name}' deleted.")
        logger.debug('using drop table function')

    def insert_many(self, df:pd.DataFrame) -> str:
        """
        Inserts multiple records into the table from a DataFrame.

        Parameters
        ----------
        df : pd.DataFrame
            The DataFrame containing the records to be inserted.

        Returns
        -------
        None
        """
        df=df.replace(np.nan, None) # for handling NULLS
        df.rename(columns=lambda x: x.lower(), inplace=True)
        columns = list(df.columns)
        logger.info(f'BEFORE the column intersection: {columns}')
        sql_column_names = [i.lower() for i in self.get_table_columns()]
        columns = list(set(columns) & set(sql_column_names))
        logger.info(f'AFTER the column intersection: {columns}')
        ncolumns=list(len(columns)*'?')
        data_to_insert=df.loc[:,columns]
    
        values=[tuple(i) for i in data_to_insert.values]
        logger.info(f'the shape of the table which is going to be imported {data_to_insert.shape}')
        # if 'geometry' in columns: #! This block is usefull in case of geometry/geography data types
        #     df['geometry'] = df['geometry'].apply(lambda geom: dumps(geom))
        #     ncolumns[columns.index('geometry')]= 'geography::STGeomFromText(?, 4326)'
        
        if len(columns)>1:
            cols,params =', '.join(columns), ', '.join(ncolumns)
        else:
            cols,params =columns[0],ncolumns[0]
            
        logger.info(f'insert structure: colnames: {cols} params: {params}')
        logger.info(values[0])
        query=f"""INSERT INTO  {self.table_name} ({cols}) VALUES ({params});"""
        
        logger.info(f'QUERY: {query}')

        self.cursor.executemany(query, values)
        try:
            for i in self.cursor.messages:
                logger.info(i)
        except:
            pass


        self.cnxn.commit()
      
        
        logger.warning('the data is loaded')
        
        def from_sql_to_pandas(self) -> pd.DataFrame:
            """
            Reads data from the SQL table and returns a pandas DataFrame.

            Returns
            -------
            pd.DataFrame
            The DataFrame containing all the data from the table.
            """
        query = f"SELECT * FROM {self.table_name}"
        df = pd.read_sql_query(query, self.cnxn)
        logger.info('Data loaded into DataFrame from SQL table.')
        return df

    def from_sql_to_pandas(self, chunksize:int, id_value:str) -> pd.DataFrame:
        """
        Reads data from the SQL table in chunks and returns a single DataFrame.

        Parameters
        ----------
        chunksize : int
            The number of rows per chunk to retrieve.
        id_value : str
            The column to order the results by.

        Returns
        -------
        pd.DataFrame
            The DataFrame containing all the data from the table.
        """
        
        offset=0
        dfs=[]
       
        
        while True:
            query=f"""
            SELECT * FROM {self.table_name}
                ORDER BY {id_value}
                OFFSET  {offset}  ROWS
                FETCH NEXT {chunksize} ROWS ONLY  
            """
            data = pd.read_sql_query(query,self.cnxn) 
            logger.info(f'the shape of the chunk: {data.shape}')
            dfs.append(data)
            offset += chunksize
            if len(dfs[-1]) < chunksize:
                logger.warning('loading the data from SQL is finished')
                logger.debug('connection is closed')
                break
        df = pd.concat(dfs)

        return df


    def update_table(self, set_values: dict, condition: str) -> None:
        """
        Updates records in the table based on a condition.

        Parameters
        ----------
        set_values : dict
            A dictionary where keys are column names and values are the new data for these columns.
        condition : str
            A string that represents the SQL WHERE condition.
        """
        set_clause = ', '.join([f"{k} = ?" for k in set_values.keys()])
        values = list(set_values.values())

        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query, values)
        self.cnxn.commit()
        logger.info('Table updated successfully.')

   
        



#primary key  hamarov, foreign key movieid
#try another movie in api

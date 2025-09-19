import os
import sys #since we have to handle the custom exception and logging
from src.pythonE2EProject.logger import logging
from src.pythonE2EProject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv #to load the environment variables from .env file
import mysql.connector


load_dotenv()
 #load the environment variables from .env file
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")

def read_sql_data():
    logging.info("Reading the data from sql database started")
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        query = "SELECT * FROM studentsperformance"
        df = pd.read_sql(query, connection)
        logging.info("connection established successfully")
        print(df.head())
        return df
    except Exception as ex:
        logging.error("Error occurred while reading data from sql database")
        raise CustomException(ex, sys)

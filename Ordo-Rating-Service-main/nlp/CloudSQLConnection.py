import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from google.cloud import storage
from mysql.connector import errorcode
import mysql.connector

config = {
  'user': os.getenv('CLOUDSQL_USER'),
  'password': os.getenv('CLOUDSQL_PASSWORD'),
  'host': os.getenv('CLOUDSQL_HOST'),
  'database': os.getenv('CLOUDSQL_DATABASE'),
  'connection_timeout': 300,
  'raise_on_warnings': True,
  'use_pure': False
}

def CloudSQLConnection():
    try:
        print('Establishing Connection...')
        cnx = mysql.connector.connect(**config)
        print('Connection Established!')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid user/password!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist!")
        else:
            print(err)
    else:
        cnx.close()
    cnx.reconnect()
    return cnx

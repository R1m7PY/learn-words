import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def sql_filling(con, data):

	

sql_connection()

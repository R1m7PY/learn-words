import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def count_table(con):
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM all_words')
	rows = cursorObj.fetchall()
	print(len(rows))

con = sql_connection()
count_table(con)
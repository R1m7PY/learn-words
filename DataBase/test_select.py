import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def count_table(con): # возвращает количество строк в таблице
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM %s' % (table))
	rows = cursorObj.fetchall()
	print(len(rows))

con = sql_connection()
table = str(input())
count_table(con)
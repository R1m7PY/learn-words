import sqlite3

from sqlite3 import Error

def sql_connection(): # подключение к БД

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def sql_output(con):

	cursorObj = con.cursor()
	cursorObj.execute('SELECT name from sqlite_master where type= "table"')
	a = cursorObj.fetchall()
	for i in range(len(a) - 2):
		print(a[i])

con = sql_connection()
sql_output(con)
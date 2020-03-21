import sqlite3

from sqlite3 import Error

def sql_connection(): # подключение к БД

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def sql_sort(con):

    	cursorObj = con.cursor()
    	cursorObj.execute('SELECT id FROM %s' % (table))
    	a = cursorObj.fetchall()
    	for i in range(len(a)):
    		print(a[i], type(a[i]))


con = sql_connection()
table = str(input("table: "))
sql_sort(con)
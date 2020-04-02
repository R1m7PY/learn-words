import sqlite3

from sqlite3 import Error

def sql_connection(): # подключение к БД

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def sql_delete_row(con):

	cursorObj = con.cursor()
	cursorObj.execute('DELETE FROM %s WHERE %s = "%s"' % (table, what, row))
	con.commit()

con = sql_connection()
table = str(input("table: "))
what = str(input("what: "))
row = str(input("row: "))
sql_delete_row(con)
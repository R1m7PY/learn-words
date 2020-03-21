import sqlite3

from sqlite3 import Error

def sql_connection(): # подключение к БД

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def checking_table(con):

	cursorObj = con.cursor()
	cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "%s"' % (table))
	con.commit()
	print(cursorObj.fetchall())

con = sql_connection()
table = str(input("table: "))
checking_table(con)
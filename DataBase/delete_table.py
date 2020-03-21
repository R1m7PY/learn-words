import sqlite3

from sqlite3 import Error

def sql_connection(): # подключение к БД

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def delete_table(con):

	cursorObj = con.cursor()
	cursorObj.execute('DROP table if exists %s' % (table))
	con.commit()
	print("table deleted")

con = sql_connection()
table = str(input("table: "))
delete_table(con)
import sqlite3

from sqlite3 import Error

def sql_connection(): # подключение к БД

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def sql_table(con): # создание новой таблицы в БД

    	cursorObj = con.cursor()
    	print("name the new table:")
    	table = str(input())
    	cursorObj.execute("CREATE TABLE %s(id integer PRINARY KEY, word, translation)" %(table))
    	con.commit()
    	print("table created")

con = sql_connection()
sql_table(con)

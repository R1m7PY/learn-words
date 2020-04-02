import sqlite3 as lite
import sys

from sqlite3 import Error

def sql_connection(): # подключение к БД

    try:

        con = lite.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def sql_sort(con):

    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM %s" %(table))
    i = 1
    while True:
        row = cursorObj.fetchone()
        
        if row == None:
            break

        print(row[1])
        cursorObj.execute("UPDATE %s SET id = %s WHERE word = '%s'" %(table, i, row[1]))
        i += 1    
        print(row[0], row[1], row[2])
    con.commit()


con = sql_connection()
table = str(input("table: "))
sql_sort(con)

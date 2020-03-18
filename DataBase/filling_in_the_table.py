import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def sql_filling(con, data): # заполнение таблицы

		cursorObj = con.cursor()
		cursorObj.execute('INSERT INTO all_words(id, word, translation) VALUES(?, ?, ?)', data)
		con.commit()

def data_filling(): # ввод данных для заполнения таблицы

	data = []
	print("filling id:")
	data.append(int(input()))
	print("filling new word:")
	data.append(str(input()))
	print("filling translation new word's:")
	data.append(str(input()))

	return data

con = sql_connection()
data = data_filling()
sql_filling(con, data)

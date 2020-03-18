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

def sql_filling(con, data): # заполнение таблицы

		cursorObj = con.cursor()
		print("specified table")
		table = str(input())
		cursorObj.execute('INSERT INTO %s(id, word, translation) VALUES(?, ?, ?)' % (table), (data))
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

def sql_update(con, update, NewWord, IDword, table):

	cursorObj = con.cursor()

	if update == 'word':
		cursorObj.execute('UPDATE %s SET word = ? where id = ?'  % (table), (NewWord, IDword))
	elif update == 'translation':
		cursorObj.execute('UPDATE %s SET translation = ? where id = ?' % (table), (NewWord, IDword))
	else:
		print("input error")

	con.commit()

def data_update():

	global update
	global NewWord

	print("specified table")
	table = str(input())
	print("what change:")
	update = str(input())
	print("how change:")
	NewWord = str(input())
	return table

def count_table(con):
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM all_words')
	rows = cursorObj.fetchall()
	return len(rows)

con = sql_connection()
answer = True

while answer == True:
	console = str(input())
	update = str()
	NewWord = str()
	IDword = int(count_table(con) + 1)

	if console == 'update':
		table = data_update()
		sql_update(con, update, NewWord, IDword, table)
		answer = True
		print("The table was updated in successfully")

	elif console == 'filling':
		data = data_filling()
		sql_filling(con, data)
		answer = True
		print("the table was filled in successfully")

	elif console == 'create table':
		sql_table(con)
		answer = True

	elif console == 'exit':
		con.close()
		answer = False

	else:
		print("This command does not exist")
		answer = True
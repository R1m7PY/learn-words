import sqlite3

from sqlite3 import Error

def sql_connection(): # подключение к БД

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

def sql_filling(con, data): # заполнение таблицы

		cursorObj = con.cursor()
		cursorObj.execute('INSERT INTO employees(id, word, translation) VALUES(?, ?, ?)', data)
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

def sql_update(con, update, NewWord, IDword):

	cursorObj = con.cursor()

	if update == 'word':
		cursorObj.execute('UPDATE employees SET word = ? where id = ?', (NewWord, IDword))
	elif update == 'translation':
		cursorObj.execute('UPDATE employees SET translation = ? where id = ?', (NewWord, IDword))
	else:
		print("input error")

	con.commit()

def data_update():

	global IDword
	global update
	global NewWord

	print("where change:")
	IDword = int(input())
	print("what change:")
	update = str(input())
	print("how change:")
	NewWord = str(input())

con = sql_connection()
update = str()
NewWord = str()
IDword = int()
answer = True

while answer == True:
	console = str(input())

	if console == 'update':
		data_update()
		sql_update(con, update, NewWord, IDword)
		answer = True

	elif console == 'exit':
		answer = False

	elif console == 'filling':
		data = data_filling()
		sql_filling(con, data)
		answer = True

	else:
		print("This command does not exist")
		answer = True
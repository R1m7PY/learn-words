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
    	cursorObj.execute("CREATE TABLE %s(id integer PRINARY KEY, word, translation)" %(table))
    	con.commit()
    	print("table created")

def sql_filling(con, data): # заполнение таблицы

		IDword = int(int(count_table(con)) + 1)
		cursorObj = con.cursor()
		cursorObj.execute('INSERT INTO %s(id, word, translation) VALUES(%s, ?, ?)' % (table, IDword), (data))
		con.commit()

def data_filling(): # ввод данных для заполнения таблицы

	data = []
	print("filling new word:")
	data.append(str(input()))
	print("filling translation new word's:")
	data.append(str(input()))

	return data

def sql_update(con, update, NewWord, IDword, table): # осн. функция замены

	cursorObj = con.cursor()

	if update == 'word':
		cursorObj.execute('UPDATE %s SET word = ? where id = ?'  % (table), (NewWord, IDword))
	elif update == 'translation':
		cursorObj.execute('UPDATE %s SET translation = ? where id = ?' % (table), (NewWord, IDword))
	else:
		print("input error")

	con.commit()

def data_update(): # доп. функция для изменения таблица

	global update
	global NewWord
	global IDword

	print("where change:")
	IDword = int(input()) # ввод строки, которая будет изменяться
	print("what change:")
	update = str(input()) # ввод столбца, в котором будут изменения 
	print("how change:")
	NewWord = str(input()) # слово замены

def count_table(con): # возвращает количество строк в таблице
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM %s' % (table))
	rows = cursorObj.fetchall()
	return len(rows)

con = sql_connection()
answer = True
print("Connecting to a table:")
table = str(input()) # подключение к таблице

while answer == True:
	console = str(input(table + " >>> ")) # ввод команды
	
# проверка введенной команды

	if console == 'update': # изменение таблицы
		NewWord = str()
		update = str()		
		data_update()
		sql_update(con, update, NewWord, IDword, table)
		answer = True
		print("The table was updated in successfully")

	elif console == 'filling': # добавление новых слов в таблицу
		data = data_filling()
		sql_filling(con, data)
		answer = True
		print("the table was filled in successfully")

	elif console == 'create table': # создание новой таблицы
		print("name new table:")
		table = str(input())
		sql_table(con)
		answer = True

	elif console == "disconnecting table": # переподключение к таблице
		print("table:")
		table = str(input())
		answer = True

	elif console == 'exit': # закрывает программу
		con.close()
		answer = False

	else:
		print("This command does not exist") # сообщает об ошибке ввода команды
		answer = True
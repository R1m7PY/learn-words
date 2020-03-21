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
    	if len(sql_checking(con)) == 0: # проверка существования таблицы
    		cursorObj.execute("CREATE TABLE %s(id integer PRINARY KEY, word, translation)" % (table))
    		con.commit()
    		print("table created")
    	else:
    		print("this table already exists")    	

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

def sql_delete(con): # функция удаления таблицы

	cursorObj = con.cursor()
	if len(sql_checking(con)) != 0: # проверка существования таблицы 
		cursorObj.execute('DROP table %s' % (table))
		con.commit()
		print("table deleted")
	else:
		print("there is no such table")

def sql_checking(con): # функция проверки существования таблицы

	cursorObj = con.cursor()
	cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "%s"' % (table))
	return cursorObj.fetchall() # возвращает массив таблиц с такими же именами
	con.commit()

def sql_output(con): # функция, возвращающая список таблиц

	cursorObj = con.cursor()
	cursorObj.execute('SELECT name from sqlite_master where type= "table"')
	a = cursorObj.fetchall()
	for i in range(len(a) - 2):
		print(a[i])

def sql_delete_row(con): # функция удаления строки

	cursorObj = con.cursor()
	cursorObj.execute('DELETE FROM %s WHERE %s = "%s"' % (table, what, row))
	con.commit()
	print("row deleted")


con = sql_connection()
answer = True
sql_output(con)
print("Connecting to a table:")
table = str(input()) # подключение к таблице

while answer == True:
	if len(sql_checking(con)) == 0: # проверка существования таблицы
		print("there is no such table")
		table = str(input("enter a different table: "))
		continue
	console = str(input(table + " >>> ")) # ввод команды
	
# проверка введенной команды

	if console == 'update': # изменение таблицы
		NewWord = str()
		update = str()		
		data_update()
		sql_update(con, update, NewWord, IDword, table)
		print("The table was updated in successfully")
		answer = True

	elif console == 'filling': # добавление новых слов в таблицу
		data = data_filling()
		sql_filling(con, data)
		print("the table was filled in successfully")
		answer = True

	elif console == 'create table': # создание новой таблицы
		print("name new table:")
		table = str(input())
		sql_table(con)
		answer = True

	elif console == "disconnecting table": # переподключение к таблице
		sql_output(con)
		print("table:")
		table = str(input())
		answer = True

	elif console == "delete table": # удаление таблицы
		sql_delete(con)
		answer = True

	elif console == "delete row": # удаление строки
		what = str(input("what: ")) # указание ключа
		row = str(input("row: ")) # значение ключа
		sql_delete_row(con)
		answer = True

	elif console == "help":
		print("update")
		print("filling")
		print("create table")
		print("disconnecting table")
		print("delete table")
		print("delete row")
		print("exit")
		print("help")
		answer = True

	elif console == 'exit': # закрывает программу
		con.close()
		answer = False

	else:
		print("This command does not exist") # сообщает об ошибке ввода команды
		answer = True
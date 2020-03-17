import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('DataBase.db')
        print('Connection is established')
        return(con)

    except Error:

        print(Error)

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
data_update()
sql_update(con, update, NewWord, IDword)
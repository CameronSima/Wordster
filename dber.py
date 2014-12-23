import sqlite3

with open('twl.txt', 'r') as f:
	read = f.readlines()

conn = sqlite3.connect('dictionary.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Dictionary
					(id INTEGER PRIMARY KEY AUTOINCREMENT,
					word text)''')

conn = sqlite3.connect('dictionary.db')
c = conn.cursor()

for x in read:
	c.execute('''INSERT INTO Dictionary (word)
					VALUES (?)''', (x,))
	conn.commit()

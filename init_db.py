import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Цветы: Что это и как с ними что-то делать', 'Ухаживать и любить')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Микропалстик. Чем он вреден для растений', 'Его много и невозможно выловить')
            )

connection.commit()
connection.close()
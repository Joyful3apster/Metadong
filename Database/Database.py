import sqlite3

connection = sqlite3.connect('Cases_Abs.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Cases
              (Fall_NR TEXT, ABS_NR INT, Textblock TEXT, Übereinstimmungen TEXT)''')

connection.commit()
connection.close()


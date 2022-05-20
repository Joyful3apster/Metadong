import sqlite3


def First_step():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Textblock(
                    Referenz_Nummer text, 
                    Absatz text)'''
                   )
    conn.commit()
    conn.close()


def add_one(Dict, name):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    for key in Dict:
        for value in Dict[key]:
            reference_key = name + "-" + key
            cursor.execute("INSERT INTO Textblock VALUES(?,?)",
                           (reference_key, value)
                           )
            conn.commit()
            conn.close()
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()


def get_rowID():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, Referenz_Nummer,Absatz FROM Textblock")
    conn.commit()
    conn.close()


def show_all():
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Textblock")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

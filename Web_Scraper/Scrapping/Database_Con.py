import sqlite3
import ppdeep


def First_step():
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE Textblock(
                    ID integer primary key autoincrement,
                    Referenz_Nummer text, 
                    Absatz text,
                    Hash text,
                    Equivalent text
                    )'''
                   )
    conn.commit()
    conn.close()


def add_one(Dict, name):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    for key in Dict:
        for value in Dict[key]:
            reference_key = name + "!" + key
            hash_value = ppdeep.hash(value)
            cursor.execute("INSERT INTO Textblock (Referenz_Nummer, Absatz, Hash, Equivalent) VALUES (?,?,?,?)",
                           (reference_key, value, hash_value, None))
            conn.commit()
            conn.close()
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()


def show_all():
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM Textblock")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


def comparer():
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    d = conn.cursor()
    for row in c.execute('SELECT * FROM Textblock'):

        if row[3] == '3::':
            continue
        else:
            Top_Ratings = []
            Tester = False
            for to_compare in d.execute('SELECT * FROM Textblock'):

                for x in row[4]:
                    if x == to_compare[0]:
                        Tester = True

                if Tester:
                    continue

                else:
                    if to_compare[0] <= row[0]:
                        continue
                    else:
                        len_row = len(row[2])
                        len_comp = len(to_compare[2])
                        if len_row >= len_comp:
                            if len_row == len_comp:
                                x = ppdeep.compare(row[3], to_compare[3])
                            else:
                                x = ppdeep.compare(row[3], ppdeep.hash(to_compare[2][:len(row[2])]))
                        else:
                            x = ppdeep.compare(ppdeep.hash(row[2][:len(to_compare[2])]), to_compare[3])
                        if x >= 65:
                            Top_Ratings.append(to_compare[0])
                        else:
                            continue
                if len(Top_Ratings) == 0:
                    string = 'None'
                else:
                    string = ''
                    for index in Top_Ratings:
                        string = string + ',' + str(index)
                    string = string[1:]
                digit = row[0]
                adder = conn.cursor()
                second_adder = conn.cursor()
                print(string)
                adder.execute('UPDATE TEXTBLOCK SET Equivalent = ? WHERE ID = ? ', (string, digit))
                for ID in Top_Ratings:
                    second_adder.execute('UPDATE TEXTBLOCK SET Equivalent = ? WHERE ID = ? ', (digit, ID))
    conn.commit()
    conn.close()

comparer()
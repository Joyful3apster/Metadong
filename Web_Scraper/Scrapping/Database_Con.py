import mysql.connector
from mysql.connector.constants import ClientFlag

def Connection_est():
    config= {'user': 'root', 'password': 'Metadrive123', 'host': '34.65.205.89', 'client_flags': [ClientFlag.SSL],
             'ssl_ca': 'ssl/server-ca (2).pem', 'ssl_cert': 'ssl/client-cert (1).pem',
             'ssl_key': 'ssl/client-key (1).pem', 'database': 'testdb'}

    cnxn = mysql.connector.connect(**config)

    return cnxn

def Insert_Data(cnxn):
    cursor = cnxn.cursor()
    query = ("INSERT INTO Cases(Fall_NR, ABS_NR ,Textblock , Übereinstimmungen)"
             "VALUES('147II234','8.2','jkhfslaksjdfa','1') ")
    cursor.execute(query)
    cnxn.commit()

def Show_TABLE(cnxn):
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM Cases')
    out = cursor.fetchall()
    for row in out:
        print(row)


Show_TABLE(Connection_est())
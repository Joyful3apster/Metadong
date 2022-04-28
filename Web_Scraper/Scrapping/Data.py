import mysql.connector
from mysql.connector.constants import ClientFlag

config={
    'user': 'root',
    'password':'Metadrive123',
    'host':'34.65.205.89',
    'client_flags':[ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca (2).pem',
    'ssl_cert': 'ssl/client-cert (1).pem',
    'ssl_key': 'ssl/client-key (1).pem'
}

cnxn = mysql.connector.connect(**config)

cursor = cnxn.cursor()
cursor.execute('CREATE DATABASE testdb')
cnxn.close()

config['database'] = 'testdb'
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()


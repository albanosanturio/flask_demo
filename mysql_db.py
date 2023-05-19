import pymysql
import json

#external file to avoid hardcoding credentials
credentials_file = open('mysql-credentials.json')
cred_load = json.load(credentials_file)

db_name = cred_load[0]['Database_name']
db_user = cred_load[0]['Database_user']
db_pass = cred_load[0]['Database_password']


conn = pymysql.connect(
    host='sql10.freesqldatabase.com',
    database=db_name,
    user=db_user,
    password=db_pass,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql_query = """ CREATE TABLE  book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""

cursor.execute(sql_query)
conn.close()
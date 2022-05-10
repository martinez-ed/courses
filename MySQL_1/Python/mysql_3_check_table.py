import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()
mycursor.execute('SHOW TABLES') # SHOW TABLES

for x in mycursor:
  print(x)

import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()

#inser a record into the table:
sql = 'INSERT INTO customers2 (name, address) VALUES (%s, %s)'
val = ('John', 'Highway 21')
mycursor.execute(sql, val)

mydb.commit() #commit the changes to the database

print(mycursor.rowcount, "record inserted.")

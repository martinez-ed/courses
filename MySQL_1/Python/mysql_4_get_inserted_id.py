import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()

sql = 'INSERT INTO customers2 (name, address) VALUES (%s, %s)'
val = ('Martinez Ed', 'Jausy Inc.')
mycursor.execute(sql, val)
mydb.commit()

#get the id of the inserted record:
print(mycursor.rowcount, 'record inserted, ID:', mycursor.lastrowid)

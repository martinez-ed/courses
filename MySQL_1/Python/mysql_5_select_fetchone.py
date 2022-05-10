import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()

#return the first row only:
mycursor.execute('SELECT name, address FROM customers2')
myresult = mycursor.fetchone()

print(myresult)

import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()

#select only the name and address columns:
mycursor.execute('SELECT name, address FROM customers2')
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

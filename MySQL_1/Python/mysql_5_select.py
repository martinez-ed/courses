import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()

#select all records from the "customers2" table, and display the result:
mycursor.execute('SELECT * FROM customers2')
myresult = mycursor.fetchall() #fetchall() method fetches all records from the query

for x in myresult:
  print(x)

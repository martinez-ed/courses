import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='',
  database='mydb2'
)
mycursor = mydb.cursor()

# sql = 'SELECT * FROM customers2 ORDER BY name'
sql = 'SELECT * FROM customers2 ORDER BY name DESC'

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

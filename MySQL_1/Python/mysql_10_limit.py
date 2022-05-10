import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='',
  database='mydb2'
)
mycursor = mydb.cursor()

#select the 5 first records from the table
# sql = 'SELECT * FROM customers2 LIMIT 5'

#start from position 3 and select the next 5 records
sql = 'SELECT * FROM customers2 LIMIT 5 OFFSET 2'
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='',
  database='mydb2'
)
mycursor = mydb.cursor()

sql = 'UPDATE customers2 SET address = %s WHERE address = %s'
adr = ('Canyon 123', 'Valley 345')

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, 'record(s) affected')

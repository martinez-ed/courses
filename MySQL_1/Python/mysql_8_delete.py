import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='',
  database='mydb2'
)
mycursor = mydb.cursor()

# sql = 'DELETE FROM customers2 WHERE address = "Jausy Inc."'
sql = 'DELETE FROM customers2 WHERE address = %s' #prevent SQL injection
adr = ('Yellow Garden 2',)

mycursor.execute(sql, adr)

mydb.commit() #is required to save the changes

print(mycursor.rowcount, "record(s) deleted")

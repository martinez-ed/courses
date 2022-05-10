import mysql.connector  

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='',
  database='mydb2'
)
mycursor = mydb.cursor()

sql = 'SELECT * FROM customers2 WHERE address = %s'
adr = ('Park Lane 38',)

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

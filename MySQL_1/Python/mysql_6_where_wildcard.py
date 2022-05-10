import mysql.connector  

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='',
  database='mydb2'
)
mycursor = mydb.cursor()

#prevent "SQL injection" by using the placeholder "%s" method:
sql = 'SELECT * FROM customers2 WHERE address LIKE %s'
adr = ('%way%',)

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

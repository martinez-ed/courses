import mysql.connector

mydb = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database = 'mydb2'
)

mycursor = mydb.cursor() #use to execute SQL

#Join "users" and "products" tables, to see the name of the users favorite product:
sql = 'SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id'
  # RIGHT JOIN products ON users.fav = products.id'
  # JOIN products ON users.fav = products.id'
  # INNER JOIN products ON users.fav = products.id'

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

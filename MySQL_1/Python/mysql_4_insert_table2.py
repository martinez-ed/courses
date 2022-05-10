import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()

#Create a table "products" with two columns "id" and "name":
sql1 = 'CREATE TABLE products (id INT, name VARCHAR(255))'

#Fill the table "products" with data:
sql2 = 'INSERT INTO products (id, name) VALUES (%s, %s)'
val = [
  (154, 'Chocolate Heaven'),
  (155, 'Tasty Lemons'),
  (156, 'Vanilla Dreams')
]

mycursor.execute(sql1)
mycursor.executemany(sql2, val)
mydb.commit()

print(mycursor.rowcount, 'records was inserted.')

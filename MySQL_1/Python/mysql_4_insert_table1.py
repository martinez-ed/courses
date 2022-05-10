import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()

#Create a table "users" with primary key "id" and two columns "name" as a string and "fav" as a integer:
sql1 = 'CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)'

#Fill the table "users" with data:
sql2 = 'INSERT INTO users (name, fav) VALUES (%s, %s)'
val = [
  ('John', '154'),
  ('Peter', '156'),
  ('Amy', '155'),
  ('Hannah', ''),
  ('Michael', '')
]

mycursor.execute(sql1)
mycursor.executemany(sql2, val)
mydb.commit()

print(mycursor.rowcount, 'records was inserted.')

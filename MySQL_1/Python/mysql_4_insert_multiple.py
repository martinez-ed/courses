import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='mydb2'
)

mycursor = mydb.cursor()

#fill the "customers2" with data:
sql = 'INSERT INTO customers2 (name, address) VALUES (%s, %s)'
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val) #executemany() method is used to insert multiple records into the table

mydb.commit()

print(mycursor.rowcount, 'records was inserted.')

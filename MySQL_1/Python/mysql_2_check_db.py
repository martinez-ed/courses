import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES") #return a list of your system's databases

#return a list of your system's databases:
for x in mycursor:
  print(x)

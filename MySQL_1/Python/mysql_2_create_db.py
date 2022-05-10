import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor() #interact with the database
mycursor.execute('CREATE DATABASE mydb2') #create a new database

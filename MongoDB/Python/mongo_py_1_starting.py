import pymongo 

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb2']

# print(myclient.list_database_names())

#check a specific database by name:
dblist = myclient.list_database_names()
if 'mydb2' in dblist:
  print('The database exists.')

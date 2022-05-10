import pymongo as pm

myclient = pm.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb2']
mycol = mydb['customers']

# mydoc = mycol.find().sort('name', 1) #1 is ascending
mydoc = mycol.find().sort('name', -1) #-1 is descending 

for x in mydoc:
  print(x)

import pymongo as pm

myclient = pm.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb2']

#create a collection
# mycol = mydb['customers']


#check if a collection exists:
# print(mydb.list_collection_names())


#check a specific collection by name:
collist = mydb.list_collection_names()
if 'customers' in collist:
  print('The collection exists.')

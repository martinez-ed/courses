import pymongo as pm

myclient = pm.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb2']
mycol = mydb['customers']

myquery = { "address": "Valley 345" }
newvalues = { '$set': { 'address': 'Jausy Inc.'} }

mycol.update_one(myquery, newvalues)

for x in mycol.find({}, {'_id': 0}):
  print(x)

import pymongo as pm

myclient = pm.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb2']
mycol = mydb['customers']

myquery = { 'address': { '$regex': '^S' } }
newvalues = { '$set': { 'name': 'Martinez-ed' } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, 'documents updated.')

for x in mycol.find({}, {'_id': 0}):
  print(x)

import pymongo as pm

myclient = pm.MongoClient("mongodb://localhost:27017/")
mydb = myclient['mydb2']
mycol = mydb['customers']

#returns the first occurrence of a matching document
mydoc = mycol.find_one()
print(mydoc)


#returns all the documents in the collection
mydoc = mycol.find()
for x in mydoc:
  print(x)


#returns only the names and addresses, not the _ids:
mydoc = mycol.find({}, {'_id': 0, 'name': 1, 'address': 1})
for x in mydoc:
  print(x)

#e.g. exclude the "address" field:
mydoc = mycol.find({}, {'address': 0})
for x in mydoc:
  print(x)

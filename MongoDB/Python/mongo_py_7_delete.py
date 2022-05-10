import pymongo as pm

myclient = pm.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb2']
mycol = mydb['customers']

# myquery = { 'address': 'Mountain 21' }
myquery = { 'address': { '$regex': '^S' } }

# x = mycol.delete_one(myquery)
x = mycol.delete_many(myquery)
#x = mycol.delete_many({}) #delete all

print(x.deleted_count, " documents deleted.")

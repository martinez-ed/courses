import pymongo as pm

myclient = pm.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb2']
mycol = mydb['customers']

myresult = mycol.find({}, {'_id': 0}).limit(5)

for x in myresult:
  print(x)

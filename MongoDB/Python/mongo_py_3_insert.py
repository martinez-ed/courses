import pymongo as pm

myclient = pm.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb2']
mycol = mydb['customers']

#insert a "document" into a collection:
# mydict = { 'name': 'John', 'address': 'Highway 37' }
mydict = { 'name': 'Peter', 'address': 'Lowstreet 27' }
x = mycol.insert_one(mydict)

print(x.inserted_id)

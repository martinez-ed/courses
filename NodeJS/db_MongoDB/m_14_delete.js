var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Delete the first customers with the address "Mountain 21":
  var myquery = { address: 'Highway 37' };
  dbo.collection('customers').deleteOne(myquery, (err, obj) => {
    if (err) throw err;
    console.log('1 document deleted');
    db.close();
  });
});
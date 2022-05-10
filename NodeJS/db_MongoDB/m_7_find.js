var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Find all documents in the "customers" collection:
  dbo.collection('customers').find({}).toArray((err, result) => {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});
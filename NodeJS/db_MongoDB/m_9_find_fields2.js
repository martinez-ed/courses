var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Exclude "address" field in the result:
  dbo.collection('customers').find({}, { projection: { address: 0 } }).toArray((err, result) => {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Find the first document in the "customers" collection:
  dbo.collection('customers').findOne({}, (err, result) => {
    if (err) throw err;
    console.log(result.name);
    db.close();
  });
});
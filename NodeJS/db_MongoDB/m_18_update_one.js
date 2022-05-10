var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Update the document with the address "Valley 345":
  var myquery = { address: 'Canyon 123' };

  //New values to update the document:
  var newvalues = { $set: { name: 'Martínez'} };

  dbo.collection('customers').updateOne(myquery, newvalues, (err, res) => {
    if (err) throw err;
    console.log("1 document updated");
    db.close();
  });
});
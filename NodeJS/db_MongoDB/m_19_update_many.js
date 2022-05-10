var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Update the document with the address begin with "S":
  var myquery = { address: /^S/ };

  //New values to update the document:
  var newvalues = { $set: { name: 'Roncancio'} };

  dbo.collection('customers').updateMany(myquery, newvalues, (err, res) => {
    if (err) throw err;
    console.log(res.result.nModified + " document(s) updated");
    db.close();
  });
});
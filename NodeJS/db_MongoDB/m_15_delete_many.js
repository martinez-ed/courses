var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Delete all customers where the address starts whith an "O":
  // var myquery = { address: /^A/ };

  //Delete all customers where the name starts whith an "V":
  var myquery = { name: /^V/ };
  
  dbo.collection('customers').deleteMany(myquery, (err, obj) => {
    if (err) throw err;
    console.log(`${obj.result.n} document(s) deleted`);
    db.close();
  });
});
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Sort the result by "name":
  var sort = { name: 1 }; //Ascending
  // var sort = { name: -1 }; //Descending
  dbo.collection('customers').find().sort(sort).toArray((err, result) => {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});
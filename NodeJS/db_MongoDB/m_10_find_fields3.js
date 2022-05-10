var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Exclude "address" field in the result:
  dbo.collection('customers').find({}, { projection: { _id: 0 } }).toArray((err, result) => {
    if (err) throw err;
    console.log(result);
    //Return the address of the third document:
    console.log(result[2].address);
    db.close();
  });
});
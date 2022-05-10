var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');

  //Return only the document with the "address" "Park Lane 38":
  var query = { address: 'Park Lane 38' };
  
  dbo.collection('customers').find(query).toArray((err, result) => {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});
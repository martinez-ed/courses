var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db("mydb1");
  
  // Create a collection named "orders":
  dbo.createCollection('orders', (err, res) => {
    if (err) throw err;
    console.log("Collection created!");
    db.close();
  });
});
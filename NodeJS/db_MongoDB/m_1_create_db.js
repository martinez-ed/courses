var MongoClient = require('mongodb').MongoClient;

//Create a database named "mydb1":
var url = "mongodb://localhost:27017/mydb1";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  console.log("Database created!");
  db.close();
});
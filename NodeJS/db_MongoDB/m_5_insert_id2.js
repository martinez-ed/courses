var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/mydb1";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');
  var myobj = [
    { _id: 1, product_id: 154, status: 1 },
    { _id: 2, product_id: 155, status: 0 },
    { _id: 3, product_id: 156, status: 1 },
    { _id: 4, product_id: 157, status: 1 },
  ];
  
  //Insert myobj array of documents:
  dbo.collection('orders').insertMany(myobj, (err, res) => {
    if (err) throw err;
    console.log(res);
  });
});
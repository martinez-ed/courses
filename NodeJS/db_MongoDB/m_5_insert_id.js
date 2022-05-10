var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/mydb1";

MongoClient.connect(url, (err, db) => {
  if (err) throw err;
  var dbo = db.db('mydb1');
  var myobj = [
    { _id: 154, name: 'Chocolate Heaven'},
    { _id: 155, name: 'Tasty Lemons'},
    { _id: 156, name: 'Vanilla Dreams'}
  ];
  
  //Insert 3 documents in a "products" collection, with specified _id:
  dbo.collection('products').insertMany(myobj, (err, res) => {
    if (err) throw err;
    //Return the result object:
    console.log(res);
  });
});
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  //Create a table where the field "id" is the primary key:
  // var sql = "CREATE TABLE customers_pk (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))";
  
  var sql = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), favorite_products INT(11))";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("Table created");
  });
});
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Left join, return all users:
  var sql = "SELECT users.name AS user, products.name AS favorite FROM users RIGHT JOIN products ON users.favorite_products = products.id";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log(result);
  });
});
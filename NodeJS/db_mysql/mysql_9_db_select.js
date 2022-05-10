var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Select all customers and return the result object:
  var sql = "SELECT * FROM customers";
  con.query(sql, function (err, result, fields) {
    if (err) throw err;
    console.log(result);
  });
  // con.query("SELECT * FROM customers", function (err, result, fields) {
  //   if (err) throw err;
  //   console.log(result);
  // });
});
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Select all customers where the address starts with an 'S':
  var sql = "SELECT *FROM customers WHERE address LIKE 'S%'";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log(result);
  });
});
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Select only "name" and "address" columns from the "customers" table:
  var sql = "SELECT name, address FROM customers";
  con.query(sql, function (err, result, fields) {
    if (err) throw err;
    // console.log(result);
    console.log(result[1].name);
    console.log(result[17].address);
  });
});
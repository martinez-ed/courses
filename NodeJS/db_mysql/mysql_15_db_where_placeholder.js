var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  var adr = 'Mountain 21';
  //Escape the address value to avoid SQL injection:
  var sql = "SELECT * FROM customers WHERE address = ?";
  //Send an array with value(s) to replace the escaped values:
  con.query(sql, [adr], function (err, result) {
    if (err) throw err;
    console.log(result);
  });
});
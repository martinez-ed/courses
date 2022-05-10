var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  var sql = "SELECT * FROM customers";
  con.query(sql, function (err, result, fields) {
    if (err) throw err;
    //Return the fields object:
    console.log(fields);
    console.log(fields[1].name);
  });
});
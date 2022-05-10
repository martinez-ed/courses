var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Sort by name ub descending order:
  var sql = "SELECT * FROM customers ORDER BY address DESC";
  con.query(sql, (err, result) => {
    if (err) throw err;
    console.log(result);
  });
});
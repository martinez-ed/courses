var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Retur the first 5 customers:
  var sql ="SELECT * FROM customers LIMIT 5";
  con.query(sql, (err, result) => {
    if (err) throw err;
    console.log(result);
  });
});
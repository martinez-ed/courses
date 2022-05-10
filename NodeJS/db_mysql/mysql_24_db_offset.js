var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Retur the first 5 customers, starting from position 4:
  // var sql ="SELECT * FROM customers LIMIT 5 OFFSET 3";
  
  //Short version:
  var sql ="SELECT * FROM customers LIMIT 3, 5";
  con.query(sql, (err, result) => {
    if (err) throw err;
    console.log(result);
  });
});
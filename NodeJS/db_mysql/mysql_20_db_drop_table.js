var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Delete the 'customers_pk' table:
  var sql = "DROP TABLE customers_pk";
  con.query(sql, (err, result) => {
    if (err) throw err;
    console.log("Table deleted");
  });
});
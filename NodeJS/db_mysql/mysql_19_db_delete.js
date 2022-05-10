var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Delete all customers with the address 'Mountain 21':
  var sql = "DELETE FROM customers WHERE address = 'Mountain 21'";
  con.query(sql, (err, result) => {
    if (err) throw err;
    console.log('Number of records deleted: ' + result.affectedRows);
  });
});
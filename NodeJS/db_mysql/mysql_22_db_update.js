var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Update the address field:
  // var sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'";

  // var sql = "UPDATE users SET favorite_products = '157' WHERE favorite_products = '154'";

  var sql = "UPDATE users SET favorite_products = '154' WHERE name = 'Ed'";
  con.query(sql, (err, result) => {
    if (err) throw err;
    console.log(result.affectedRows + " record(s) updated");
  });
});
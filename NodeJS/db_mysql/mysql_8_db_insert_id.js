var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  var sql = "INSERT INTO customers (name, address) VALUES ('Natalia', 'Chiquinquira 19')";
  con.query(sql, function (err, result) {
    if (err) throw err;
    //Use the result object to get the ID of the last inserted record:
    console.log("1 record inserted, ID: " + result.insertId);
  });
});
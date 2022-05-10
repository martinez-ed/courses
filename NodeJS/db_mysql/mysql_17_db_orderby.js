var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  //Sort result by name:
  var sql = "SELECT * FROM customers ORDER BY name";
  con.query(sql, (err, result) => {
      if (err) throw err;
      console.log(result);
    });
});
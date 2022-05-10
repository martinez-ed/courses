var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb1"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  //Make SQL statement:
  // var sql = "INSERT INTO customers (name, address) VALUES ?";
  // //Make an array of values:
  // var values = [
  //   ['John', 'Highway 71'],
  //   ['Ed', 'Main st, 45'],
  //   ['Peter', 'Lowstreet 4'],
  //   ['Amy', 'Apple st 652'],
  //   ['Hannah', 'Mountain 21'],
  //   ['Michael', 'Valley 345'],
  //   ['Sandy', 'Ocean blvd 2'],
  //   ['Betty', 'Green Grass 1'],
  //   ['Richard', 'Sky st 331'],
  //   ['Susan', 'One way 98'],
  //   ['Vicky', 'Yellow Garden 2'],
  //   ['Ben', 'Park Lane 38'],
  //   ['William', 'Central st 954'],
  //   ['Chuck', 'Main Road 989'],
  //   ['Viola', 'Sideway 1633']
  // ];

  // var sql = "INSERT INTO users (name, favorite_products) VALUES ?";
  // //Make an array of values:
  // var values = [
  //   ['John', '154'],
  //   ['Ed', '154'],
  //   ['Peter', '154'],
  //   ['Amy', '155'],
  //   ['Hannah', ''],
  //   ['Michael', '']
  // ];
  var sql = "INSERT INTO products (id, name) VALUES ?";
  //Make an array of values:
  var values = [
    ['154', 'Chocolate heaven'],
    ['155', 'Tasty Lemons'],
    ['156', 'Vanilla Dreams'],
    ['157', 'Strawberry Dreams'],
  ];
  //Execute the SQL statement, with the value array:
  con.query(sql, [values], function (err, result) {
    if (err) throw err;
    console.log("Number of records inserted: " + result.affectedRows);
  });
});
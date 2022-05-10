var http = require('http');
var uc = require('upper-case');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  //Use our upper-case module to convert the string to uppercase
  res.write(uc.upperCase('Hello new World!'));
  res.end();
}).listen(8080);
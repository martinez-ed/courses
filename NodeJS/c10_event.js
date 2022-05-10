var fs = require('fs');
var rs = fs.createReadStream('./files/demofile.txt');
rs.on('open', function () {
  console.log('The file is open');
});
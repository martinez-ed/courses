var fs = require('fs');

fs.writeFile('./files/demofile.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
});
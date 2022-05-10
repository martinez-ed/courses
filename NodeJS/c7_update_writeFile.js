var fs = require('fs');

fs.writeFile('./files/mynewfile3.txt', 'This is my new text.', function (err) {
  if (err) throw err;
  console.log('Replaced!');
});
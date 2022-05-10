var nodemailer = require('nodemailer');;

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'dev.martinezed@gmail.com',
    pass: 'pacoRavan3423*'
  }
});

var mailOptions = {
  from: 'dev.martinezed@gmail.com',
  to: 'edeyeme@gmail.com, ed@jausy.com',
  subject: 'Sending Email using Node.js',
  // text: 'That was easy!'
  html: '<h1>Welcome</h1><p>That was easy!</p>'
};

transporter.sendMail(mailOptions, function (error, info) {
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
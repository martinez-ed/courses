// Try and catch
// Syntax: 
// try {
//     code to try
// } catch (error) {
//     code to handle the error
// }
// The try statement allows you to execute code that might throw an error.
// The catch statement allows you to handle the error.
// The try statement can have multiple catch statements.


// The finally Statement:
// The finally statement is executed after the try and catch statements, regardless of whether an error occurred.
// Syntax:
// try {
//     code to try
// } catch (error) {
//     code to handle the error
// } finally {
//     code to be executed regardless of the result
// }


// The throw Statement:
// The throw statement throws an error.
// Syntax:
// throw error;


// The Error Object:
// Properties: name, message.

// Syntax:
// var error = new Error();
// error.name = "Error";
// error.message = "Error message";
// error.stack = "Error stack";


// RangeError - A number "out of range" has occurred.
let num =1;
try {
  num.toPrecision(500); //number can't have 500 significant digits
} catch (error) {
  console.log(error.name); // RangeError
  console.log(error.message); // toPrecision() argument must be between 1 and 100
}


// ReferenceError - A reference to an invalid variable has occurred.
let x = 5;
try {
  x = y + 1; // y is not defined
} catch (error) {
  console.log(error.name); // ReferenceError
  console.log(error.message); // y is not defined
}


// SyntaxError - The code in eval() is invalid.
try {
  eval("alert('Hello)"); //missing closing '
} catch (error) {
  console.log(error.name); // SyntaxError
  console.log(error.message); // Invalid or unexpected token
}


// TypeError - A value of the wrong type has occurred.
num = 1;
try {
  num.toUpperCase(); //can't convert number to upper case
} catch (error) {
  console.log(error.name); // TypeError
  console.log(error.message); // num.toUpperCase is not a function
}


// URIError - A malformed URI has occurred.
try {
  decodeURI("%%%"); //can't decode URI percent signs
} catch (error) {
  console.log(error.name); // URIError
  console.log(error.message); // URI malformed
}

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


// Style Guides ---------------------------------------------------------------
// Variable and function names should be camelCase.
// All names start with a lowercase letter.
// var myVariable = "Hello";


// Spaces arround operators always put spaces around them, and after commas. DON'T USE TABULATION.
// let myVariable = y + z;


// Code indentation always use two (2) spaces of code blocks.
// function toCelsius(fahrenheit) {
//   return (fahrenheit - 32) * 5 / 9;
// }


// Statements Rules ------------------------------------------------------------
// Simple statements end with a semicolon.

// const cars = ["BMW", "Volvo", "Ford"];
// const person = {
//   name: "John",
//   age: 30
// };

// Complex statements
// Put the opening bracket at the end of the line.
// Use one space before the opening bracket.
// Put the closing blacket on a new line, without leading spaces.
// Don't end with a semicolon.

// loops:
// for (let i = 0; i < 5; i++) {
//   x += i;
// }

// Conditionals:
// if (time < 20) {
//   console.log("It's early");
// } else {
//   console.log("It's late");
// }


// Object Rules ---------------------------------------------------------------
// Place the opening bracket on the same line as the object name.
// Use colon plus one space between each property and its value.
// Use quotes arround string values, not arround numeric values.
// Don't add a comma after the last property-value pair.
// Place the closing bracket on a new line, without leading spaces.
// Always end an object definition with a semicolon.

// const person = {
//   firstName: "John",
//   lastName: "Doe",
//   age: 30,
//   eyeColor: "blue"
// };

// Short objects can be written compressed:
// const person = {firstName:"John", lastName:"Doe", age:30};


// Line Lenght < 80 characters --------------------------------------------------
// For readability, avoid lines longer than 80 characters.
// The best place to break a line is after an operator or a comma.

// document.getElementById("myElement").innerHTML =
// "Hello World.";


// Naming Conventions ---------------------------------------------------------
// Variable and function names written in camelCase.
// Globar variables written in UPPERCASE.
// Constants written in UPPERCASE. (e.g. PI).


// Loading JavaScript in HTML ------------------------------------------------
// <script src="js/script.js"></script>


// Use Lower Case File Names --------------------------------------------------
// Use lower case file names for JavaScript files.



// JavaScript Best Practices ---------------------------------------------------
// Avoid "global variables", avoid "new", avoid "==", avoid "eval()".
// Always declare Local Variables.


// Declarations on top ---------------------------------------------------------
// Put all declarations at the top of each script or function.
// Give cleaner code.
// Provide a single place to look for local variables.
// Make it easier to avoid unwanted (implied) global variables.
// Reduce the possibility of unwanted re-declarations.

// E.g. Block of code >>>>>>>>>>>>>>>>
// Declare at the beginning:
let firstName, lastName, price, discount, fullPrice;

// Use later:
firstName = "John";
lastName = "Doe";
price = 19.99;
discount = 0.10;
fullPrice = price * (1 - discount);

console.log(fullPrice);

// Initialize Variables on top:
// Initialice variables when you declare them.
// Give cleaner code.
// Provide a single place to look and initialize variables.
const myArray = [];
const myObject = {};


// Declare Objects and Arrays with "const" ------------------------------------------------
// Will prevent any acccidental change of type.

//e.g. object:
const car = {type: "sedan", color: "red", model: "X5"};
// car = 'BMW'; // Error: Assignment to constant variable.

//e.g. array:
const cars = ["BMW", "Volvo", "Ford"];
// cars = 3; // Error: Assignment to constant variable.


// Don't use "new Object()" -----------------------------------------------------
// Use "" or ''- instead of "new String()".
// Use 0 - instead of "new Number()".
// Use false - instead of "new Boolean()".
// Use {} - instead of "new Object()".
// Use [] - instead of "new Array()".
// Use /()/ - instead of "new RegExp()".
// Use function() - instead of "new Function()".


// Beware of automatic type conversion ------------------------------------------
// JavaScript is loosely typed.
// A variable can contain all data types.
// A variable can change its data types.
// Numbers can accidentally be converted to strings.
// JavaScript can convert numbers to strings.

let xyz = 'Hello'; // typeof xyz is string
xyz = 5; // typeof xyz is number

let zyx = 5 + "7"; // zyx.valueOf() is "57", typeof zyx is string
zyx = "5" - 7; // zyx.valueOf() is "-2", typeof zyx is number


// Use "===" Comparison Operator ------------------------------------------------
// The "==" operator always converts (to matching types) before comparing.
// The "===" operator force comparison of values and type.
0 == ""; // true
0 === ""; // false


// Use Parameter Default Values ------------------------------------------------
// The value of the missing argument is set to undefined.
// Undefined values can break code.
// Assign a default value to a parameter or argument.
function myFunction(x, y) {
  if (y === undefined) {
    y = 0;
  } else {
    x = x + y;
  }
}


// Always end your "switch" statement with a "default" case. Event if you think there is no need for it.


// Avoid Number, String, and Boolean as "Objects" ----------------------------------
// Always treat numbers, strings, and booleans as primitive values.
// Declaring these types as objects, slows down execution speed.
// let x = new Number(5);
// let y = new String("Hello");


// Avoid using "eval()" --------------------------------------------------------
// This function is used to run text as a script, but it is not recommended.
// It is not secure.
// It allows arbitrary code to be run.



// COMMON MISTAKES ------------------------------------------------------------

// Accidentally using the assignment operator.
// An assignment always return the value of the assignment.
// let x = 0;
// if (x == 10)

// Forget that switch statement use strict comparison.
// let x = 10;
// switch (x) {
//   case "10": alert("Hello"); // Error: "10" is not a number.
// }


// Confusing Addition and Concatenation:
// Addition is about adding numbers.
// Concatenation is about adding strings.
// let x = 10;
// x = 10 + 5; // 15
// x += "5"; // "105"


// Misunderstanding Floats:
// Numbers are stored as 64-bits floating point numbers (Floats).
// All programming languages, have difficulties with precise floating point values.
// let x = 0.1 + 0.2; // 0.30000000000000004

// Solve the problem above, it helps to multiply and divide:
// let z = (x * 10) / 10; // 0.3


// Breaking a String into Parts:
// let x =
// "Hello World!";

// Use a "backslash" to break a statement in a string:
// let x = "hello \
// world!";


// Ending definition with a comma:
// Trailing commas in object and array definition are legal.
// JSON does not allow trailing commas.
// person = {firstName: "John", lastName: "Doe", age: 30}
// points = [40, 100, 1, 5, 25, 10];
// JSON e.g.:
// person = {'firstName': 'John', 'lastName': 'Doe', 'age': 30}



// PERFORMANCE ---------------------------------------------------------------
// REDUCE ACTIVITY IN LOOPS:
// Statements or assignments that can be placed outside the loop will make the loop run faster.

// Bad code:
// for (let i = 0; i < arr.length; i++) {

// Better code:
// let myLength = arr.length;
// for (let i = 0; i < myLength; i++) {


// REDUCE DOM ACCESS:
// Accessing  the HTML DOM is very slow.
// Access it once, use it as local variable.

// const obj = document.getElementById("myId");
// obj.innerHTML = "Hello World!";


// REDUCE DOM SIZE:
// Keep the number of elements in the HTML DOM to a minimum.
// Remove elements that are not used.


// Avoid unnecessary variables:
// Don't create variables that are not used.


// Delay JavaScript Loading:
// Putting your script at the bottom of the page body lets the browser load the page first.

// If possible, you can add your script to the page by code, after the page has loaded:
// <script>
// window.onload = function() {
//   const element = document.createElement("script");
//   element.src = "myScript.js";
//   document.body.appendChild(element);
// };
// </script>

// Comparison Operators
// ==, ===, !=, !==, >, <, >=, <=


// Logical Operators
// &&, ||, !


// Conditional Operator (ternary)
// variable = (condition) ? value1 : value2;
let age = 17
let ageStatus = (age >= 18) ? 'You can vote!' : 'You cannot vote!';
console.log('ageStatus: ' + ageStatus);

//e.g. Convert to the proper type before comparing two strings:
let voteable
// let age1 = '17';
// let age1 = 19;
let age1 = 'james';
let num = Number(age1);
if (isNaN(num)) {
  voteable = 'Not a number';
} else {
  voteable = (num >= 18) ? 'You can vote!' : 'You cannot vote!';
}
console.log(voteable);


// "if" statement
// if (condition) {
  // code to run if condition is true
// }

let hour = new Date().getHours();
let greeting;

//e.g. Make a "Good day" greeting if the hour is less than 18:00:
if (hour < 18) {
  greeting = 'Good day!';
}
console.log(greeting);


// "else" statement
// if (condition) {
  // code to run if condition is true
// }
// else {
  // code to run if condition is false
// }

//e.g. If the hour is less than 18, make a "Good day" greeting, otherwise make a "Good evening" greeting:
if (hour < 18) {
  greeting = 'Good day!';
} else {
  greeting = 'Good evening!';
}
console.log(greeting);


// "else if" statement
// if (condition1) {
  // code to run if condition1 is true
// } else if (condition2) {
  // code to run if condition1 is false and condition2 is true
// } else {
  // code to run if condition1 is false and condition2 is false
// }

//e.g. If the hour is less than 18, make a "Good day" greeting, if the hour is less than 21, make a "Good evening" greeting, otherwise make a "Good night" greeting:
if (hour < 18) {
  greeting = 'Good day!';
} else if (hour < 21) {
  greeting = 'Good evening!';
} else {
  greeting = 'Good night!';
}
console.log(greeting);

//e.g. If time is less than 10:00, create a "Good morning" greeting, if not, but time is less than 16:00, create a "Good afternoon" greeting, otherwise create a "Good evening" greeting:
if (hour < 10) {
  greeting = 'Good morning!';
} else if (hour < 16) {
  greeting = 'Good afternoon!';
} else {
  greeting = 'Good evening!';
}
console.log(greeting);


// "switch" statement
// switch (expression) {
  // case value1:
    // code to run if expression is value1
    // break;
  // case value2:
    // code to run if expression is value2
    // break;
  // case value3:
    // code to run if expression is value3
    // break;
  // default:
    // code to run if expression is not value1, value2, or value3
// }

//e.g. Calculate the weekday name:
let day = new Date().getDay();
let weekday;
switch (day) {
  case 0:
    weekday = 'Sunday';
    break;
  case 1:
    weekday = 'Monday';
    break;
  case 2:
    weekday = 'Tuesday';
    break;
  case 3:
    weekday = 'Wednesday';
    break;
  case 4:
    weekday = 'Thursday';
    break;
  case 5:
    weekday = 'Friday';
    break;
  case 6:
    weekday = 'Saturday';
    break;
  default:
    weekday = 'Invalid day';
}
console.log(weekday);


// Strict Comparison Operator (===)
let x = '0';
let text;
switch (x) {
  case 0:
    text = 'Off';
    break;
  case 1:
    text = 'On';
    break;
  default:
    text = 'No value found';
}
console.log(text);

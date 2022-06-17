// "typeof" Operator:
// The typeof operator returns a string indicating the type of the operand.
// The typeof operator is used in expressions.
// The typeof operator returns one of the following values:
typeof 'John'; // "string"
typeof 3.14; // "number"
typeof NaN; // "number"
typeof true; // "boolean"
typeof [1, 2, 3]; // "object"
typeof { name: 'John', age: 30 }; // "object"
typeof new Date(); // "object"
typeof function myFunc() {}; // "function"
typeof myVar; // "undefined"
typeof null; // "object"
typeof undefined; // "undefined"


// Assets ---------------------------------------------------------//
let x;
const fruits = ['Apple', 'Banana', 'Orange'];
// ---------------------------------------------------------------//


// "constructor" Property:
// The constructor property returns the function that created an object.
x = 'John';
console.log(x.constructor); // function String() { [native code] }
x = 3.14;
console.log(x.constructor); // function Number() { [native code] }
x = true;
console.log(x.constructor); // function Boolean() { [native code] }
x = [1, 2, 3];
console.log(x.constructor); // function Array() { [native code] }
x = { name: 'John', age: 30 };
console.log(x.constructor); // function Object() { [native code] }
x = new Date();
console.log(x.constructor); // function Date() { [native code] }
x = function myFunc() {};
console.log(x.constructor); // function Function() { [native code] }

//e.g. Check the constructor property to find out if an object is an Array:
function isArray(myArr) {
  return myArr.constructor === Array;
}
console.log(isArray(fruits)); // true



// TYPE CONVERSION ------------------------------------------------//

// "Number()" convert strings to numbers:
console.log(Number('3.14')); // 3.14
console.log(Number('')); // 0
console.log(Number(" ")); // 0
console.log(Number('99 88')); // NaN

// "String()" convert numbers to strings:
console.log(String(x = 3.14)); // "3.14"
console.log(String(123)); // "123"
console.log(String(100 + 23)); // "123"

// "toString()" convert numbers to strings:
console.log(x.toString()); // "3.14"
console.log((123).toString()); // "123"
console.log((100 + 23).toString()); // "123"

// Convert "Boolean" to "Number":
console.log(Number(true)); // 1
console.log(Number(false)); // 0

// Convert "Number" to "Boolean":
console.log(Boolean(1)); // true
console.log(Boolean(0)); // false


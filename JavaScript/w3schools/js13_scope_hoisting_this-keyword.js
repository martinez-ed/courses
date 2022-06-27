// JavaScript has 3 types of scope:
// 1. Block scope
// 2. Function scope
// 3. Global scope


// BLOCK SCOPE
// ES6 introduced two important keywords: "let" and "const".
// let is used to declare a variable that is block scoped.
// const is used to declare a variable that is block scoped and immutable.


// LOCAL SCOPE
// A local scope is a scope that is defined within a function.
//e.g:
// function myFunc() {
//   let carName = 'BMW';
    // code here CAN use carName
// }
// code here CANNOT use carName


// FUNCTION SCOPE
// A function scope is a scope that is defined within a function.
//e.g:
// function myFunc() {
//   var carName = 'BMW'; // Function scope
//   function innerFunc() {
//     let carName = 'Audi'; // Local scope
//   }
// }
// code here CANNOT use carName


// GLOBAL SCOPE
// A global scope is a scope that is defined outside of a function.
//e.g:
// const carName = 'BMW'; // Global scope
// function myFunc() {
//   let carName = 'Audi'; // Local scope
  // code here CAN use carName
// }
// code here CAN use carName


// Automatically Global Scope
// When a variable is declared outside of a function, it is automatically global.
//e.g:
// myFunction();

// code here CAN use carName
// function myFunction() {
//   carName = 'BMW'; // Global scope
// }
// code here CAN use carName


// HOISTING
// Hoisting is JavaScript's default behavior of moving declarations to the top.
// To avid bugs, always declare all variables at the beginning of every scope.



// THIS KEYWORD --------------------------------------------//
// "this" is a keyword that refers to the current object.
// "this" is being invoked (used or called).
const person = {
  firstName: 'John',
  lastName: 'Doe',
  id: 5566,
  fullName: function() {
    return this.firstName + ' ' + this.lastName;
  }
}
console.log(person.fullName());


// Use "this" in Event Handlers:
// <button onclick="this.style.display='none'">
//   Click to hide me!
// </button>


// Explicit Function Binding:
// The "call()" and "apply()" methods allow you to explicitly bind a function to a particular object.
const person1 = {
  fullName: function() {
    return this.firstName + ' ' + this.lastName;
  }
}
const person2 = {
  firstName: 'Ed',
  lastName: 'Smith'
}
console.log(person1.fullName.call(person2)); // Ed Smith


// Function Borrowing:
// With the "bind()" method, an object can borrow a method from another object.
const person3 = {
  firstName: 'Natalie',
  lastName: 'Smith'
}
//use bind to another object:
let fullName = person.fullName.bind(person3);
console.log(fullName()); // Natalie Smith


// This Precedence:
// 1. bind()
// 2. apply() and call()
// 3. object method
// 4. global scope

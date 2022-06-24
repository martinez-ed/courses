// Creating an Array - Syntax:

// const arr = [item1, item2, ...];
// const arr = new Array(length);
// const arr = Array(length);


// A declaration can span multiple lines:
const cars1 = [
  'Ford',
  'Chevy',
  'Honda',
  'Toyota'
];
console.log(cars1);


// Create an array, and then provide the elements:
const cars2 = [];
cars2[0] = 'Ford';
cars2[1] = 'Chevy';
cars2[2] = 'Honda';
cars2[3] = 'Toyota';
console.log(cars2);


// Accessing Array Elements
let car = cars2[1];
console.log(car); // Chevy


// Changing Array Elements
cars2[1] = 'BMW';
console.log(cars2); // [ 'Ford', 'BMW', 'Honda', 'Toyota' ]


// Objects
// An object is a collection of name/value pairs.
const person1 = {
  firstName: 'John',
  lastName: 'Doe',
  age: 50,
  eyeColor: 'blue'
};
console.log(person1);

// Array elements can be objects:
// myArray[0] = Date.now(); // objects in an array
// myArray[1] = myfuction(); // functions in an array
// myArray[2] = myCar; // arrays in an array


const fruits = ['Apple', 'Banana', 'Orange', 'Pear'];


// myArray.length; // number of elements in the array
let lenghtFruits = fruits.length;
console.log(lenghtFruits); // 4


// Accessing the first element of an array:
let firstFruit = fruits[0];
console.log(firstFruit); // Apple
// Accesing the last element of an array:
let lastFruit = fruits[fruits.length - 1];
console.log(lastFruit); // Pear


// Looping through an array, using a for loop:
for (let i = 0; i < fruits.length; i++) {
  console.log(i+1, fruits[i]);
}


// Looping through an array, using a forEach loop:
fruits.forEach(function(fruit, index) {
  console.log(index+1, fruit);
});


// Adding an element to an array:

// push() - adds an element to the end of an array
fruits.push('Kiwi');
console.log(fruits); // [ 'Apple', 'Banana', 'Orange', 'Pear', 'Kiwi' ]

// length property can add an element to the end of an array:
fruits[fruits.length] = 'Kiwi2';
console.log(fruits); // [ 'Apple', 'Banana', 'Orange', 'Pear', 'Kiwi', 'Kiwi2' ]


// Diferennce between Arrays and Objects:
// Arrays are used when you need to access elements by index (elements), while objects are used when you need to access elements by name (properties).


// Recognizing an Array:

// The typeof operator returns the type of a variable:
console.log(typeof fruits); // object

// The Array.isArray() method determines whether the passed value is an Array:
console.log(Array.isArray(fruits)); // true

// The instanceof operator returns true if the object is an instance of the specified class:
console.log(fruits instanceof Array); // true

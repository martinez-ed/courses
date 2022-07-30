// JavaScript Object Maps ------------------------------------------------------------
// A Map is a data structure for storing key-value pairs.
// A Map remembers the order in which the keys were inserted.


// Map Methods:
// new Map() - Creates a new Map object.
// set() - Adds a new value for a key.
// get() - Returns the value associated with a key.
// clear() - Removes all elements from the map.
// delete() - Removes a value associated with a key.
// has() - Returns true if a key exists.
// forEach() - Invokes a callback for each key/value pair.
// entries() - Returns an iterator object with the [key, value] pairs.
// keys() - Returns an iterator object with the keys.
// values() - Returns an iterator object with the values.

// Map Properties:
// size - Returns the number of elements in the map.
// prototype - Returns the prototype of the map.
// constructor - Returns the constructor of the map.


// Create a Map:
const fruits = new Map(
  [['apple', 500], ['banana', 300], ['orange', 200]]
);
console.log(fruits);


// Add a new element:
fruits.set('grape', 100);
console.log(fruits);


// Get the value of a key:
console.log(fruits.get('apple'));


// Change existing Map value:
fruits.set('apple', 1000);
console.log(fruits); // Map { 'apple' => 1000, 'banana' => 300, 'orange' => 200, 'grape' => 100 }


// Removes a Map element:
fruits.delete('apple');
console.log(fruits); // Map { 'banana': 300, 'orange': 200, 'grape': 100 }


// Check if a key exists:
console.log('Exists apple: ' + fruits.has('apple')); // false
console.log('Exists banana: ' + fruits.has('banana')); // true


// Maps are objects:
console.log(typeof fruits); // object
console.log(fruits instanceof Map); // true


// Iterate through the Map: (forEach)
let text = "";
fruits.forEach(function(value, key) {
  text += key + ": " + value + " | ";
});
console.log('forEach: ' + text); // forEach: apple: 1000 | banana: 300 | orange: 200 | grape: 100 |


// Iterate through the Map: (entries)
text = "";
for (const x of fruits.entries()) {
  text += x[0] + ": " + x[1] + " | ";
  // text += x;
}
console.log('entries: ' + text); // entries: apple: 1000 | banana: 300 | orange: 200 | grape: 100 |


// Iterate through the Map: (keys)
text = "";
for (const x of fruits.keys()) {
  text += x + ', ';
}
console.log('keys: ' + text); //keys: apple, banana, orange, grape,


// Iterate through the Map: (values)
text = "";
for (const x of fruits.values()) {
  text += x + ", ";
}
console.log('values: ' + text); //values: 1000, 300, 200, 100,

//e.g. Sum all the values in the Map:
let sum = 0;
for (const x of fruits.values()) {
  sum += x;
}
console.log('sum: ' + sum); //sum: 2200


// OBJECTS AS KEYS:
// Being able to use objects as keys is an important Map feature.
// The key can be any object, including functions.

//create Objects:
const apples = { name: 'Apples' };
const bananas = { name: 'Bananas' };
const oranges = { name: 'Oranges' };

//create a Map:
const fruitsMap = new Map();

//add elements to the Map:
fruitsMap.set(apples, 500);
fruitsMap.set(bananas, 300);
fruitsMap.set(oranges, 200);

//get the value of "apples" (an object):
console.log('Value of apples: ' + fruitsMap.get(apples)); //Value of apples: 500

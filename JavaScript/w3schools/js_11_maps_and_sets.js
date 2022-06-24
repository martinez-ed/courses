// Set Methods:
// new Set(iterable) - Creates a new set object.
// add(value) - Adds a value to the set.
// delete(value) - Deletes a value from the set.
// has(value) - Returns true if the set contains the value.
// forEach(callback[, thisArg]) - Calls a function for each element in the set.
// values() - Returns an iterator over the values in the set.


// Assets -------------------------------------------------- //
let letters, txt, myMap; // initializations
// --------------------------------------------------------- //


// "new Set()" Method

//1. Passing an Array to new Set():
letters = new Set(['a', 'b', 'c', 'd', 'e']);
console.log(letters); // Set(5) { 'a', 'b', 'c', 'd', 'e' }

//2. Create a new Set and use "add()" to add values:
letters = new Set();
letters.add('a'); // "add()" Method
letters.add('b');
letters.add('c');
letters.add('z');
console.log(letters); // Set(4) { 'a', 'b', 'c', 'z' }

//3. Create a new Set and use "add()" to add variables:
letters = new Set();
const a = 'a';
const b = 'b';
const c = 'c';

letters.add(a);
letters.add(b);
letters.add(c);
console.log(letters); // Set(3) { 'a', 'b', 'c' }


// "forEach()" Method
txt = '';
letters = new Set(['a', 'b', 'c', 'd', 'e']);

letters.forEach(function(value, key, set) {
  txt += value + ' ';
});
console.log(txt); // a b c d e


// "values()" Method
txt = '';
for (let x of letters.values()) {
  txt += x + ' ';
}
console.log(txt); // a b c d e



// Map Methods -------------------------------------------------- //
// new Map() - Creates a new map object.
// set(key, value) - Sets a value to a key.
// get(key) - Returns the value of a key.
// has(key) - Returns true if the map contains the key.
// delete(key) - Deletes a key from the map.
// forEach(callback[, thisArg]) - Calls a function for each element in the map.
// entries() - Returns an iterator with the [key, value] pairs.

// Create a new Map and use "set()" to add values:
myMap = new Map();
myMap.set('apple', 500);
myMap.set('banana', 100);
myMap.set('orange', 300);
console.log(myMap); // Map(3) { 'apple' => 500, 'banana' => 100, 'orange' => 300 }


// "set()" Change the value of a key:
myMap.set('apple', 1000);
console.log(myMap); // Map(3) { 'apple' => 1000, 'banana' => 100, 'orange' => 300 }


// "get()" Method
console.log(myMap.get('apple')); // 1000


// "has()" Method
console.log(myMap.has('apple')); // true

myMap.delete('apple');
console.log(myMap.has('apple')); // false
console.log(myMap.size); // 2


// "forEach()" Method
txt = '';
myMap.set('kiwi', 444);
myMap.forEach(function(value, key, map) {
  txt += key + ':' + value + ' ';
});
console.log(txt); // banana:100 orange:300 kiwi:444

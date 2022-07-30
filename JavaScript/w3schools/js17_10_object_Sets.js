// ---------------------------------------------------------
// 17.10 - OBJECT SET
// ---------------------------------------------------------
// A set is an unordered collection of unique values.

// Set Methods:
// new Set() - Creates a new Set object.
// add() - Adds a new element to the set.
// delete() - Removes an element from the set.
// has() - Returns true if a value exists.
// clear() - Removes all elements from the set.
// forEach() - Invokes a callback for each element.
// values() - Returns an iterator with all the values.
// keys() - Same as values().
// entries() - Returns an iterator with the [key, value] pairs.

// Set properties:
// size - Returns the number of elements in the set.


// Create a Set:
const letters = new Set(['a', 'b', 'c']);
console.log(letters.size); // 3

// Add an element to the Set:
letters.add('d');
console.log(letters.size); // 4

// Add variables to the Set:
let e = 'e';
letters.add(e);
console.log(letters.size); // 5


// The forEach() Method:
// Invokes a callback function for each element in the set.
let text = "";
letters.forEach(function(value) {
  text += value;
});
console.log('forEach(): ' + text); // abcde


// The values() Method:
// Returns an iterator with all the values.
text = "";
for (let value of letters.values()) {
  text += value + " | ";
}
console.log('values(): ' + text); // abcde


// The keys() Method: Same as values().
// Set has no keys.
// This make Sets compatible with Maps.


// The entries() Method: A Set has no keys.
// Returns [value, value] pairs.
text = "";
for (let entry of letters.entries()) {
  text += entry + " | ";
}
console.log(text); // a,a | b,b | c,c | d,d | e,e |


// Sets are Objects:
// For a Set, "typeof" returns "object":
console.log('typeof letters: ' + typeof letters); // object

// For a Set, "instanceof" returns true:
console.log('letters instanceof: ' + (letters instanceof Set)); // true

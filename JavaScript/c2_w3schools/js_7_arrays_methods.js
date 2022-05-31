// Array methods
const fruits = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruits);


// toString() method converts an array to a string.
// arr.toString() 
console.log(fruits.toString()); // Banana,Orange,Apple,Mango


// join() method converts an array to a string.
// arr.join(separator)
console.log(fruits.join(' * ')); // Banana * Orange * Apple * Mango


// pop() method removes the last element from an array.
// arr.pop()
console.log(fruits.pop()); // Mango
console.log(fruits); // Banana,Orange,Apple


// push() method adds a new element to an array (at the end).
// arr.push(element)
console.log(fruits.push("Kiwi")); // 4
console.log(fruits); // Banana,Orange,Apple,Kiwi


// shift() method removes the first element from an array.
// arr.shift()
console.log(fruits.shift()); // Banana
console.log(fruits); // Orange,Apple,Kiwi


// unshift() method adds a new element to an array (at the beginning).
// arr.unshift(element)
console.log(fruits.unshift("Strawberry")); // 4
console.log(fruits); // Strawberry,Orange,Apple,Kiwi


// concat() method joins two or more arrays.
// arr.concat(arr1, arr2, ...)
const girls = ['Cecilie', 'Lone'];
const boys = ['Emil', 'Tobias', 'Linus'];
const childs = girls.concat(boys);
console.log(childs);
//e.g. Merging an Array with Values:
const merginChild = boys.concat('Peter');
console.log(merginChild);


// splice() method can be used to add new items to an array.
// arr.splice(position, removed, 'new1', 'new2',...)
console.log('Original Array:', fruits); // Strawberry,Orange,Apple,Kiwi
let removed = fruits.splice(2, 2, 'Lemon', 'Mango');
console.log('After splice():', fruits); // Strawberry,Orange,Lemon,Mango
console.log('Removed:', removed); // Apple,Kiwi


// slice() method can be used to extract part of an array.
// arr.slice(start, end)
let sliceFruits = fruits.slice(1,3);
console.log('slice():', sliceFruits); // Orange,Lemon


// sort() method sorts the items of an array.
// arr.sort()
let sortFruits = fruits.sort();
console.log('sort():', sortFruits); // Apple,Banana,Lemon,Mango,Orange,Strawberry


// reverse() method reverses the items of an array.
// arr.reverse()
let reverseFruits = fruits.reverse();
console.log('reverse():', reverseFruits); // Mango,Orange,Lemon,Strawberry,Banana,Apple


// Numeric Sort
const points = [40, 100, 1, 5, 25, 10];

// Compare function:
// arr.sort(function(a, b){return a-b}) "Asending"
// arr.sort(function(a, b){return b-a}) "Desending"
// arr.sort(function(a, b){return 0.5 - Math.random()}) "Random"
points.sort(function(a, b){return a-b});
console.log(points); // 1, 5, 10, 25, 40, 100

// The Fisher-Yates shuffle:
for (let i = points.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [points[i], points[j]] = [points[j], points[i]];
}
console.log(points); // 1, 5, 10, 25, 40, 100


// Highest and lowest values:
let highest = points.sort(function(a, b){return b-a})[0];
let lowest = points.sort(function(a, b){return a-b})[0];
console.log('Highest:', highest); // 100
console.log('Lowest:', lowest); // 1

// Use the Math.max() and Math.min() methods:
let highest2 = Math.max(...points);
let lowest2 = Math.min(...points);
console.log('Highest with Math.max():', highest2); // 100
console.log('Lowest with Math.min():', lowest2); // 1


// Sorting Object Arrays
const cars = [
    {type: 'Volvo', year: 2016},
    {type: 'Toyota', year: 2019},
    {type: 'Saab', year: 2001},
    {type: 'BMW', year: 2010}
];

// Write a "Compare Function" to compare the property values:
cars.sort(function(a, b){return a.year-b.year});
console.log('Sorted by year:', cars);

// Comparing string properties:
cars.sort(function(a, b){return a.type.localeCompare(b.type)});
console.log('Sorted by type:', cars);

const nums = [45, 4, 9, 16, 25];


// "forEach()" method calls a function (a callback function) once for each array element.
// arr.forEach(function(value, index, array){
//     // statements
// })
nums.forEach(function(value, index, array) { //callback function
  console.log(`${index+1}: ${value}`);
});


// "map()" method creates a new array with the results of calling a function for each array element.
function myMap(value, index, array) { //callback function
  return value * 2; //multiply each element by 2
}
const nums2 = nums.map(myMap);
console.log(nums2);


// "filter()" method creates a new array with all array elements that pass a test (provided as a function).
function myFilter(value) { //callback function
  return value > 18; //elements greater than 18
}
const nums3 = nums.filter(myFilter);
console.log(nums3);


// "reduce()" method applies a function against an accumulator and each element in the array (from left to right) to reduce it to a single value.
function myReduce(accumulator, value) { //callback function
  return accumulator + value; //sum of all numbers
}
const nums4 = nums.reduce(myReduce);
console.log('Sum of all numbers: ' + nums4);

// Can accept an initial value:
const nums5 = nums.reduce(myReduce, 100);
console.log('Sum of all numbers: ' + nums5);


// "every()" method check if all array values pass a test.
function myEvery(value) { //callback function
  return value > 18; //elements greater than 18
}
const nums6 = nums.every(myEvery);
console.log('All over 18 is: ' + nums6);


// "some()" method check if any array value passes a test.
function mySome(value) { //callback function
  return value > 18; //elements greater than 18
}
const nums7 = nums.some(mySome);
console.log('Any over 18 is: ' + nums7);


const fruits = ['Apple', 'Banana', 'Orange', 'Apple', 'Durian'];


// "indexOf()" returns the first index at which a given element can be found in the array, or -1 if it is not present.
//arr.indexOf(item, start)

let position = fruits.indexOf('Apple') + 1;
console.log(`The position of 'Apple' is: ${position}`);


// "lastIndexOf()" returns the last index at which a given element can be found in the array, or -1 if it is not present.
let position2 = fruits.lastIndexOf('Apple') + 1;
console.log(`The last position of 'Apple' is: ${position2}`);


// "find()" returns the value of the first element in the array that satisfies the provided testing function. Otherwise undefined is returned.
function myFind(value) { //callback function
  //sort the array and find the first element greater than 18:
  return value.sort((a, b) => a - b).find(value => value > 18);
}
console.log(nums);
console.log('The first element greater than 18 is: ' + myFind(nums));


// "findIndex()" returns the index of the first element in the array that satisfies the provided testing function. Otherwise -1 is returned.
function myFindIndex(value) { //callback function
  return value.sort((a, b) => a - b).findIndex(value => value > 18);
}
console.log(nums);
console.log('First number over 18 has index: ' + myFindIndex(nums));


// "Array.from()" creates an array from an array-like or iterable object.
const arrayLike = {
  0: 'a',
  1: 'b',
  2: 'c',
  length: 3
};
const arr = Array.from(arrayLike);
console.log(arr); //['a', 'b', 'c']

const arr2 = Array.from('hello');
console.log(arr2); //['h', 'e', 'l', 'l', 'o']


// "Array.keys()" returns an array of a given object's own enumerable property names.
const keys = fruits.keys();
let text = '';
for (let key of keys) {
  text += key + ' ';
}
console.log(text); //0 1 2 3 4


// "Array.entries()" returns an array of a given object's own enumerable property [key, value] pairs, in the same order as that provided by a for...in loop.
const entries = fruits.entries();
let text2 = '';
for (let entry of entries) {
  text2 += entry + ' ';
}
console.log(text2); //0 Apple 1 Banana 2 Orange 3 Apple 4 Durian


// "Array.values()" returns an array of a given object's own enumerable property values.
const values = fruits.values();
let text3 = '';
for (let value of values) {
  text3 += value + ' ';
}
console.log(text3); //Apple Banana Orange Apple Durian


// "Array.includes()" determines whether an array contains a certain element, returning true or false as appropriate.
let inc1 = fruits.includes('Orange'); //true
let inc2 = fruits.includes('Lemon'); //false
console.log(inc1, inc2);

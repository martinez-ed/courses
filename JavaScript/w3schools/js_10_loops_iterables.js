// for - loop through a block of code a number of times
// for/in - loop through the properties of an object
// for/of - loop through the values of an iterable object
// while - loop through a block of code while a condition is true
// do/while - loop through a block of code at least once, then check the condition


// Assets -------------------------------------------------- //
const cars = ['BMW', 'Volvo', 'Saab', 'Ford', 'Ferrari', 'Audi'];
let i, len, txt, myString, y; // initializations
const person = {name:'John', age:30, city:'New York'};
const nums = [45, 4, 9, 16, 25];
// --------------------------------------------------------- //


// FOR LOOP
// for (initialization; condition; increment) {
//   // code to run
// }
for (let i = 0; i < cars.length; i++) {
  console.log(i+1, cars[i]);
}

// Initiate many values in "initialization":
for (i=0, len=cars.length, txt=''; i<len; i++) {
  txt += cars[i] + ' | ';
}
console.log(txt);

// Omit "initialization", values are set before the loop starts:
i = 3;
len = cars.length;
txt = '';
for (; i<len; i++) {
  txt += cars[i] + ' - ';
}
console.log(txt);

// Omit "increment":
i = 0;
len = cars.length;
txt = '';
for (; i<len;) {
  txt += cars[i] + ' * ';
  i++;
}
console.log(txt); // BMW * Volvo * Saab * Ford * Ferrari * Audi


// FOR/IN LOOP
// for (key in object) {
//   // code to run
// }
txt = '';
for (let x in person) {
  txt += x + ': ' + person[x] + ' ';
}
console.log(txt); // name: John age: 30 city: New York

// For In Over Array
txt = '';
for (let x in nums) {
  txt += nums[x] + ' ';
}
console.log(txt); // 45 4 9 16 25


// FOREACH LOOP
// array.forEach(myFunction);
txt = '';
function myFunction(item, index, array) {
  txt += item + ' - ';
}
nums.forEach(myFunction);
console.log(txt); // 45 - 4 - 9 - 16 - 25 -


// FOR OF LOOP
// for (variable of iterable) {
//   // code to run
// }
txt = '';
for (let x of nums) {
  txt += x + ' ';
}
console.log(txt); // 45 4 9 16 25

// Looping Over Strings
txt = '';
myString = 'JavaScript';
for (let x of myString) {
  txt += x + '_';
}
console.log(txt); // J a v a S c r i p t


// WHILE LOOP
// while (condition) {
//   // code to run
// }
txt = '';
y = 0;
while (y < nums.length) {
  txt += 'Number ' + y + ' ';
  y++;
}
console.log('While Loop: ' + txt); // Number 0 Number 1 Number 2 Number 3 Number 4


// DO/WHILE LOOP
// do {
//   // code to run
// } while (condition);
txt = '';
i = 0;
do {
  txt += 'Number ' + i + ' ';
  i++;
} while (i < nums.length);
console.log('Do/While: ' + txt); // Number 0 Number 1 Number 2 Number 3 Number 4


// Comparing For and While Loops
i = 0;
txt = '';
for (; cars[i];) {
  txt += cars[i] + ' ';
  i++;
}
console.log('For Loop: ' + txt); // BMW Volvo Saab Ford Ferrari Audi

i = 0;
txt = '';
while (cars[i]) {
  txt += cars[i] + ' ';
  i++;
}
console.log('While Loop: ' + txt); // BMW Volvo Saab Ford Ferrari Audi


// BREAK and CONTINUE
// break - Used to jump out of a loop
txt = '';
for (let i=0; i<10; i++) {
  if (i === 3) {
    break;
  }
  txt += i + ' ';
}
console.log('Break: ' + txt); // 0 1 2

// continue - Used to breaks one iteration of a loop, if a specified condition occurs, and continue to the next iteration.
txt = '';
for (let i=0; i<10; i++) {
  if (i === 3) {
    continue;
  }
  txt += i + ' ';
}
console.log('Continue: ' + txt); // 0 1 4 5 6 7 8 9

// Break can be used to jump out of any code block:
txt = '';
list: {
  txt += cars[0] + ' ';
  txt += cars[1] + ' ';
  break list;
  txt += cars[2] + ' ';
  txt += cars[3] + ' ';
}
console.log('Break: ' + txt); // BMW Volvo



// ITERABLES 
// An object that can be iterated over, such as a string, array, map, set, or even a generator function.

// Iterating over a string:
myString = 'W3Schools.com';
txt = '';
for (let x of myString) {
  txt += x + ' ';
}
console.log(txt); // W 3 S c o l l s . c o m


// Iterating over an array:
txt = '';
for (const x of cars) {
  txt += x + ' - ';
}
console.log(txt); // BMW Volvo Saab Ford Ferrari Audi


// Iterating over a Set:
txt = '';
const mySet = new Set(['a', 'b', 'c']);
for (const x of mySet) {
  txt += x + ' ';
}
console.log(txt); // a b c


// Iterating over a Map:
txt = '';
const myMap = new Map([
  ['a', 1],
  ['b', 2],
  ['c', 3]
]);
for (const x of myMap) {
  txt += x + ' ';
}
console.log(txt); // a,1 b,2 c,3
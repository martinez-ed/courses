// ---------------------------------------------------------
// 17.9 - OBJECT ITERABLES
// ---------------------------------------------------------
// An object is iterable if it has a method called Symbol.iterator.
// The "Symbol.iterator" is a function that returns a "next()" method.
// The "next()" method returns an object with two properties:
// value: The value returned by the iterator.
// done: A boolean indicating whether the iterator is finished or not.

//create an Object:
const myNums = {};

//make it iterable:
myNums[Symbol.iterator] = function() {
  let i = 0;
  done = false;
  return {
    next() {
      i += 10;
      if (i == 100) { done = true; }
      return { value: i, done: done };
    }
  };
}

// The Symbol.iterator method is called automatically by the for...of loop:

//create an iterator using for..of:
let text = '';
for (let num of myNums) {
  text += num + ' ';
}
console.log(text); // 10 20 30 40 50 60 70 80 90


//do it manually:
let myIterator = myNums[Symbol.iterator]();
text = '';
while (true) {
  let result = myIterator.next();
  if (result.done) { break; }
  text += result.value + ' ';
}
console.log(text); // 10 20 30 40 50 60 70 80 90

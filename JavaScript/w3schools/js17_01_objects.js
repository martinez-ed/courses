// A JavaScript object is a collection of named values.
// It's a common practice to declare objects with the "const" keyword.


// Using an Object Literal:
const person = {
  firstName: "John", // property
  lastName : "Doe",
  age      : 50,
  eyeColor : "blue",
  fullName : function() { // method
    return this.firstName + " " + this.lastName;
  }
};
console.log(person.firstName);
console.log(person.fullName());

//e.g. Create an empty object and then add properties to it:
const car = {};
car.make = "Ford";
car.model = "Mustang";
car.year = 1969;
car.color = "red";
car.fullName = function() {
  return this.make + " " + this.model;
}
console.log(car.fullName());


// Objects are mutable:
// Any change to x will also change person, because they are pointing to the same object:
const x = person;
x.firstName = "Jane";
console.log(person.fullName());


// Adding and Deleting Properties:
const person2 = {
  firstName: "John",
  lastName : "Doe",
  age      : 50,
  eyeColor : "blue"
};
person2.nationality = "Colombia";
delete person2.age; //or delete person['age'];


// for...in loop:
// The for...in loop is used to loop through the properties of an object.
let txt = "";
for (let x in person2) {
  txt += person2[x] + " ";
}
console.log(txt);


// Nested Objects:
const person3 = {
  firstName: "John",
  lastName : "Doe",
  cars: {
    car1: "Ford",
    car2: "BMW",
    car3: "Fiat"
  }
};
let p1 = 'car2';
console.log(person3.cars.car2);
console.log(person3.cars["car2"]); //or person3['cars']['car2']
console.log(person3.cars[p1]); //or person3['cars'][p1]


// Nested Arrays and Objects:
const person4 = {
  firstName: "John",
  age: 41,
  cars: [
    { brand: "Ford", models: ["Fiesta", "Focus", "Mustang"] },
    { brand: "BMW", models: ["320", "X3", "X5"] },
    { brand: "Fiat", models: ["500", "Panda"] }
  ]
};
console.log(person4.cars[0].models[1]); //Focus


//Use a for-in loop to access inside the nested objects:
let y = "";
for (let i in person4.cars) {
  y += "\n" + person4.cars[i].brand + ": ";
  for (let j in person4.cars[i].models) {
    y += person4.cars[i].models[j] + " - ";
  }
}
console.log(y);


// Using Built-in Object Methods:
let message = "Hello World";
let msg = message.toUpperCase();
console.log(msg);

person.upperN = person.fullName().toUpperCase();
console.log(person.upperN);


// Displaying the object in a Loop:
txt = "";
for (let x in person) {
  // you must use person[x]
  // person.x will not work, because x is a variable
  txt += person[x] + " ";
}
console.log(txt);


// Using Object.values():
// The Object.values() method returns an array of a object's property values.
const myArray = Object.values(person);
console.log(myArray); // ["Jane", "Doe", 50, "blue", [Function: fullName], "JANE DOE"]


// Using JSON.stringify():
// Can be stringified (converted to a string) to be stored in a file or database with the JSON notation.
// Will not stringify functions. (fullName is a function)
let myJSON = JSON.stringify(person);
console.log(myJSON); // {"firstName":"John","lastName":"Doe","age":50,"eyeColor":"blue","upperN":"JOHN DOE"}


// Stringify Dates:
person.today = new Date();
myJSON = JSON.stringify(person);
console.log(myJSON); // {"firstName":"John","lastName":"Doe","age":50,"eyeColor":"blue","upperN":"JOHN DOE","today":"2019-01-01T00:00:00.000Z"}


// Stringify Functions:
// Will not stringify functions. (fullName is a function)
// Before stringifying the function.
person.fullName = person.fullName.toString();
myJSON = JSON.stringify(person);
console.log(myJSON); // {"firstName":"John","lastName":"Doe","age":50,"eyeColor":"blue","upperN":"JOHN DOE","today":"2019-01-01T00:00:00.000Z","fullName":"function fullName() { return this.firstName + \" \" + this.lastName; }"}


// Stringify Arrays:
const arr = ['John', 'Peter', 'Sally', 'Jane'];
let myString = JSON.stringify(arr);
console.log(myString); // ["John","Peter","Sally","Jane"]

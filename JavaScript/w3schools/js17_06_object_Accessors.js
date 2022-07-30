// WHY USE GETTERS AND SETTERS? --------------------------------------------------
// Getters and setters allow you to get and set object properties via methods.
// It gives simpler syntax
// It alows equal syntax for properties and methods
// It can secure better data quality

const person5 = {
  firstName: "John",
  lastName : "Doe",
  language : "EN",
  get lang() {
    return this.language;
  }
};
console.log(person5.lang); // EN

const person6 = {
  firstName: "John",
  lastName : "Doe",
  language : "",
  set lang(lang) {
    this.language = lang;
  }
};
// Set an object property using a setter:
person6.lang = "FR";
console.log(person6.language); // FR


// FUNCTION OR GETTER AND SETTER:
// Example 1 access "fullName" as a function: person.fullName().
// Example 2 access "fullName" as a getter: person.fullName.
// The second example provides a simpler syntax.

// Example 1:
const personX = {
  firstName: "John",
  lastName : "Doe",
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
console.log(personX.fullName()); // John Doe

// Example 2:
const personY = {
  firstName: "John",
  lastName : "Doe",
  get fullName() {
    return (this.firstName + " " + this.lastName).toUpperCase();
  }
};
console.log(personY.fullName); // JOHN DOE

let myJSON2 = JSON.stringify(personY);
console.log(myJSON2); // {"firstName":"John","lastName":"Doe","fullName":"JOHN DOE"}


// Object.defineProperty():
// The Object.defineProperty() method defines a new property directly on an object, or modifies an existing property on an object, and returns the object.
// The method takes three arguments:
// 1. object: The object on which to define the property.
// 2. property: The name of the property to be defined or modified.
// 3. descriptor: An object that describes the property being defined or modified.

//define object:
const obj = { counter : 0 };

//define getters and setters:
Object.defineProperty(obj, 'reset', {
  get : function () { this.counter = 0; }
});
Object.defineProperty(obj, 'increment', {
  get : function () { this.counter++; }
});
Object.defineProperty(obj, 'decrement', {
  get : function () { this.counter--; }
});
Object.defineProperty(obj, 'add', {
  set : function (value) { this.counter += value; }
});
Object.defineProperty(obj, 'subtract', {
  set : function (value) { this.counter -= value; }
});

//play with the counter:
obj.reset;
obj.add = 5;
obj.subtract = 1;
obj.increment;
obj.decrement;
console.log('Counter: ' + obj.counter); // Counter: 4
console.log(JSON.stringify(obj)); // {"counter":4}

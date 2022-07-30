// Assets -----------------------------------------------------
let person = {
  firstName: 'John',
  lastName: 'Doe',
  age: 50,
  eyeColor: 'blue',
  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }
};
// ------------------------------------------------------------


// MANAGING OBJECTS -------------------------------------------

// Create object with an existing object as prototype:
// Object.create(prototype)
//example:
let person2 = Object.create(person);
person2.firstName = 'Jane';
person2.lastName = 'Doe';
person2.age = 30;
person2.eyeColor = 'green';
console.log('My name is ' + person2.fullName + ' and I am ' + person2.age + ' years old.'); // My name is Jane Doe and I am 30 years old.


// Adding or changing an object property:
// Object.defineProperty(object, property, descriptor)
//example:
Object.defineProperty(person, 'year', {value: '2022'});
console.log('My year is ' + person.year); // My year is 2022


// Adding or changing object properties:
// Object.defineProperties(object, descriptors)
//example:
Object.defineProperties(person, {
  fullName: {
    value: 'Edwin Martínez',
    writable: false,
    enumerable: true,
    configurable: true
  },
  age: {
    value: 41,
    writable: false,
    enumerable: true,
    configurable: true
  }
});
console.log('My name is ' + person.fullName + ' and I am ' + person.age + ' years old.'); // My name is Edwin Martínez and I am 41 years old.


// Accessing Properties:
// Object.getOwnPropertyDescriptor(object, property)
//example:
let descriptor = Object.getOwnPropertyDescriptor(person, 'fullName');
console.log(descriptor); // {value: 'Edwin Martínez', writable: false, enumerable: true, configurable: true}
console.log(descriptor.value); // Edwin Martínez


// Returns all properties as an array:
// Object.getOwnPropertyNames(object)
//example:
let properties = Object.getOwnPropertyNames(person2);
console.log(properties); // [ 'firstName', 'lastName', 'age', 'eyeColor']
console.log(properties.length); // 4


// Accessing the prototype:
// Object.getPrototypeOf(object)
//example:
let prototype = Object.getPrototypeOf(person2);
console.log(prototype); // { firstName: 'John', lastName: 'Doe', age: 41, eyeColor: 'blue', fullName: 'Edwin Martínez' }


// Returns enumerable properties as an array:
// Object.keys(object)
//example:
Object.defineProperty(person2, 'age', {enumerable: false});

let keys = Object.keys(person2);
console.log(keys); // [ 'firstName', 'lastName', 'eyeColor' ]
console.log(keys.length); // 3

keys = Object.keys(person);
console.log(keys); // [ 'firstName', 'lastName', 'age', 'eyeColor', 'fullName' ]
console.log(keys.length); // 5



// PROTECTING OBJECTS -----------------------------------------

// Prevents adding or removing properties:
// Object.preventExtensions(object)
//example:
Object.preventExtensions(person);
person.age = 30;
console.log(person.age); // 41


// Returns true if properties can be added or removed:
// Object.isExtensible(object)
//example:
console.log(Object.isExtensible(person)); // false
console.log(Object.isExtensible(person2)); // true


// Prevents changes of object properties (not values):
// Object.seal(object)
//example:
Object.seal(person2);
person2.age = 32;
console.log(person2.age); // 32


// Returns true id object is sealed:
// Object.isSealed(object)
//example:
console.log(Object.isSealed(person2)); // true
console.log(Object.isSealed(person)); // false


// Prevents any changes to an object:
// Object.freeze(object)
//example:
Object.freeze(person2);
person2.age = 33;
console.log(person2.age); // 32


// Returns true if object is frozen:
// Object.isFrozen(object)
//example:
console.log(Object.isFrozen(person2)); // true
console.log(Object.isFrozen(person)); // false


// Adding Getters and Setters -----------------------------------
// The "Object.defineProperty()" method can be used to add getters and setters to an object.

// Create an object:
const userNew = {
  firstName: 'Michael',
  lastName: 'Jackson'
};

// Define a getter:
Object.defineProperty(userNew, 'fullName', {
  get: function() {
    return `${this.firstName} ${this.lastName}`;
  }
});

console.log(userNew.fullName); // Michael Jackson

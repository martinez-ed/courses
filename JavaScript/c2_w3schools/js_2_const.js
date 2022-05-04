// Create an array:
const cars = ["Saab", "Volvo", "BMW"];
console.log(cars);
// Change an element:
cars[0] = "Opel";
console.log(cars);


// Create a const object:
const car = {
  type: 'Fiat',
  model: '500',
  color: 'white'
};
console.log(car);
// Change a property:
car.color = 'red';
console.log(car);
// Add a property:
car.year = '2018';
console.log(car);

// e.g. Function, calculate the product of two numbers:
function multiply(a, b) {
  return a * b;
}
let result = multiply(2, 3);
console.log('The result is: ' + result);

// e.g. Function, convert Fahrenheit to Celsius:
function convertFtoC(f) {
  return (f - 32) * 5 / 9;
}
let change = convertFtoC(32);
console.log(change);

// e.g. Object, create a new object:
const person = {
  firstName: 'John',
  lastName: 'Doe',
  age: 30,
  eyeColor: 'blue'
};
console.log(person);
// Access a property: object.property or object["property"]
console.log(person.age);
console.log(person["eyeColor"]);

// Add a property like object method:
person.fullName = function () {
  return this.firstName + ' ' + this.lastName;
}
// Accesssing object method: object.method()
console.log(person.fullName());

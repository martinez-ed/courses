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

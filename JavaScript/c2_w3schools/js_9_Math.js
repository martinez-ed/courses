// Properties (Constants):

// Math.E; - returns Euler's number
console.log('Math.E: ' + Math.E); // 2.718281828459045
// Math.PI; - returns PI
console.log('Math.PI: ' + Math.PI); // 3.141592653589793
// Math.SQRT2; - returns the square root of 2
console.log('Math.SQRT2: ' + Math.SQRT2); // 1.4142135623730951
// Math.SQRT1_2; - returns the square root of 1/2
console.log('Math.SQRT1_2: ' + Math.SQRT1_2); // 0.7071067811865476
// Math.LN2; - returns the natural logarithm of 2
console.log('Math.LN2: ' + Math.LN2); // 0.6931471805599453
// Math.LN10; - returns the natural logarithm of 10
console.log('Math.LN10: ' + Math.LN10); // 2.302585092994046
// Math.LOG2E; - returns the base-2 logarithm of E
console.log('Math.LOG2E: ' + Math.LOG2E); // 1.4426950408889634
// Math.LOG10E; - returns the base-10 logarithm of E
console.log('Math.LOG10E: ' + Math.LOG10E); // 0.4342944819032518


// Math methods - Math.method(parameter):

// Number to integer; 4 commmon methods:

// Math.round(x); - rounds x to the nearest integer
console.log('Math.round(4.6): ' + Math.round(4.6)); // 5
// math.ceil(x); - rounds x up to the nearest integer
console.log('Math.ceil(4.4): ' + Math.ceil(4.4)); // 5
// Math.floor(x); - rounds x down to the nearest integer
console.log('Math.floor(4.6): ' + Math.floor(4.6)); // 4
// Math.trunc(x); - rounds x to an integer towards zero
console.log('Math.trunc(4.6): ' + Math.trunc(4.6)); // 4


// Math.sign(x); - returns if x is negative, null or positive
console.log('Math.sign(4.6): ' + Math.sign(4.6)); // 1
console.log('Math.sign(0): ' + Math.sign(0)); // 0
console.log('Math.sign(-4.6): ' + Math.sign(-4.6)); // -1


// Math.pow(x, y); - returns x to the power of y
console.log('Math.pow(2, 3): ' + Math.pow(2, 3)); // 8


// Math.sqrt(x); - returns the square root of x
console.log('Math.sqrt(9): ' + Math.sqrt(9)); // 3


// Math.cbrt(x); - returns the cube root of x
console.log('Math.cbrt(8): ' + Math.cbrt(8)); // 2


// Math.hypot(x, y); - returns the length of the hypotenuse of the right triangle with sides x and y
console.log('Math.hypot(3, 4): ' + Math.hypot(3, 4)); // 5


// Math.sin(x); - returns the sine of x
console.log('Math.sin(Math.PI / 2): ' + Math.sin(Math.PI / 2)); // 1
// Math.cos(x); - returns the cosine of x
console.log('Math.cos(Math.PI / 2): ' + Math.cos(Math.PI / 2)); // -1
// Math.tan(x); - returns the tangent of x
console.log('Math.tan(Math.PI / 4): ' + Math.tan(Math.PI / 4)); // 1
// Math.asin(x); - returns the arc sine of x
console.log('Math.asin(1): ' + Math.asin(1)); // 1.5707963267948966
// Math.acos(x); - returns the arc cosine of x
console.log('Math.acos(1): ' + Math.acos(1)); // 0
// Math.atan(x); - returns the arc tangent of x
console.log('Math.atan(1): ' + Math.atan(1)); // 0.7853981633974483


// Math.abs(x); - returns the absolute value of x
console.log('Math.abs(-4.6): ' + Math.abs(-4.6)); // 4.6


// Math.min(x, y, z, ...); - returns the smallest of the arguments
console.log('Math.min(4, 6, -1, -2): ' + Math.min(4, 6, -1, -2)); // -2
// Math.max(x, y, z, ...); - returns the largest of the arguments
console.log('Math.max(4, 6, -1, -2): ' + Math.max(4, 6, -1, -2)); // 6


// Math.log(x); - returns the natural logarithm of x
console.log('Math.log(2): ' + Math.log(2)); // 0.6931471805599453



// Math.random(); - returns a random number between 0 and 1
console.log('Math.random(): ' + Math.random()); // 0.9087370018098

//e.g. Return a random integer from 0 to 9:
let randomNum = Math.floor(Math.random() * 10);
console.log('Random number: ' + randomNum);

//e.g. Return a random integer from 0 to 10:
let randomNum2 = Math.floor(Math.random() * 11);
console.log('Random number: ' + randomNum2);


// Proper Random Function - use for all random integer pursoses:
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}
console.log('Random number: ' + getRandomInt(0, 10));

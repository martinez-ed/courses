// Infinity
let myNum = 2;
let txt = '';
while (myNum < Infinity) {
    myNum *= myNum;
    txt += myNum + '\n';
}
console.log(txt);

// Hexadecimal
// Hexadecimal numbers are represented by a prefix of 0x, followed by a sequence of digits from 0 to 9 and from A to F.
let x = 0xFF;
console.log(x); // 255

// Use the toString() method to output numbers from base 2 to base 36:
let num = 32;
console.log('Binary (base 2): ' + num.toString(2)); // 100000
console.log('Octal (base 8): ' + num.toString(8)); // 40
console.log('Decimal (base 10): ' + num.toString(10)); // 32
console.log('Duodecimal (base 12): ' + num.toString(12)); // 28
console.log('Hexadecimal (base 16): ' + num.toString(16)); // 20
console.log('Duotrigesimal (base 32): ' + num.toString(32)); // 10
console.log('Hexatrigesimal (base 36): ' + num.toString(36)); // w

// toString()
// Syntax: number.toString([radix])
let num1 = 123;
console.log(num1.toString()); // 123
console.log((123).toString()); // 123
console.log((100 + 23).toString()); // 123


// toExponential() 
// Syntax: numberObject.toExponential([fractionDigits])
let num2 = 9.656;
console.log(num2.toExponential()); // 1.23456789e+4
console.log(num2.toExponential(2)); // 1.23e+4
console.log(num2.toExponential(4)); // 1.2346e+4
console.log(num2.toExponential(6)); // 1.23457e+4


// toFixed()
// Syntax: number.toFixed([fractionDigits])
let num3 = 9.656;
console.log(num3.toFixed()); // 10
console.log(num3.toFixed(2)); // 9.66
console.log(num3.toFixed(4)); // 9.6560
console.log(num3.toFixed(6)); // 9.656000


// toPrecision()
// Syntax: number.toPrecision([precision])
let num4 = 9.656;
console.log(num4.toPrecision()); // 9.656
console.log(num4.toPrecision(2)); // 9.7
console.log(num4.toPrecision(4)); // 9.656
console.log(num4.toPrecision(6)); // 9.65600


// valueOf()
// Syntax: number.valueOf()
let num5 = 123;
console.log(num5.valueOf()); // 123
console.log((123).valueOf()); // 123
console.log((100 + 23).valueOf()); // 123


// Converting Variables to Numbers, 3 methods:

// Number() - syntax: Number(value)
// can be used to convert JavaScript variables to numbers.
console.log(Number(true)); // 1
console.log(Number(false)); // 0
console.log(Number(null)); // 0
console.log(Number(undefined)); // NaN
console.log(Number('')); // 0
console.log(Number('123')); // 123
console.log(Number('123.45')); // 123.45
console.log(Number('    123.45    ')); // 123.45
console.log(Number('123.45    ')); // 123.45
console.log(Number('    123.45abc    ')); // NaN
console.log(Number('123,45')); // NaN
console.log(Number('John')); // NaN

// Number() Method used on Date object:
// returns the number of milliseconds since 1.1.1970
// let d = new Date('1970-01-01');
let d = new Date('1970-01-02'); // 86400000 milliseconds
console.log(Number(d)); // 1 day
let d2 = new Date('2017-09-30'); // 15067296e5 milliseconds
console.log(Number(d2));

// parseInt() - syntax: parseInt(value, radix)
// parses a string and returns a whole number.
console.log(parseInt('-10')); // -10
console.log(parseInt('-10.33')); // -10
console.log(parseInt('10)')); // 10
console.log(parseInt('10.33')); // 10
console.log(parseInt('10 6')); // 10
console.log(parseInt('10.33 6')); // 10
console.log(parseInt('10 years')); // 10
console.log(parseInt('years 10')); // NaN

// parseFloat() - syntax: parseFloat(value)
// parses a string and returns a number. Spaces are ignored. Only the first number is returned.
console.log(parseFloat('10')); // 10
console.log(parseFloat('10.33')); // 10.33
console.log(parseFloat('10 20 30')); // 10
console.log(parseFloat('10 years')); // 10
console.log(parseFloat('years 10')); // NaN

// Number.isFinite()
// Number.isInteger()
// Number.isNaN()
// Number.isSafeInteger()

// Number object:
let y = 500;
let z = new Number(500); // Number object
console.log(y == z); // true
console.log(y === z); // false

// Number Properties:
// Number.constructor - Returns the Number function.
// Number.MAX_VALUE - Returns the largest number that can be represented in JavaScript.
// Number.MIN_VALUE - Returns the smallest number that can be represented in JavaScript.
// Number.NEGATIVE_INFINITY - Returns the negative Infinity value.
// Number.POSITIVE_INFINITY - Returns the positive Infinity value.
// Number.NaN - Returns the Not-a-Number value.
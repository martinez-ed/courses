// Bitwise

// Bitwise operators are used to perform bitwise operations on binary numbers.
// The bitwise operators are:
// & - Bitwise AND
// | - Bitwise OR
// ^ - Bitwise XOR
// ~ - Bitwise NOT
// << - Left shift
// >> - Right shift
// >>> - Zero fill right shift


// Converting Decimal to Binary:
function decToBin(dec) {
  return (dec >>> 0).toString(2);
}
console.log(decToBin(-5));


// Converting Binary to Decimal:
function binToDec(bin) {
  return parseInt(bin, 2).toString(10);
}
console.log(binToDec(101));


// Assets ---------------------------------------------------------//
let srt, regex, result;
// ---------------------------------------------------------------//

// Regular expressions are used to match patterns in strings.

// Syntax: /pattern/modifiers
// - A pattern is a string of characters.
// - A modifier is a string of characters that can be used to modify the pattern.


// Using String "search()" with a string:
str = "The quick brown Fox jumps over the lazy dog.";
regex = /fox/i;
result = str.search(regex);
console.log('Using String "search()" with a string: ' + result);


// Using String "replace()" with a string:
srt = "Visit Microsoft!";
regex = /microsoft/i;
result = srt.replace(regex, "Google");
console.log(srt);
console.log('Using String "replace()" with a string: ' + result);


// Regular Expression Modifiers:
// i - Case insensitive
// g - Global
// m - Multiline
// u - Unicode
// y - Sticky
// s - Dot matches all characters
// x - Ignore whitespace and comments
// A - Automatically add ^ and $ to pattern
// B - Automatically add ^ to pattern
// E - Automatically add $ to pattern
// L - Automatically add ^ and $ to pattern and make uppercase
// M - Automatically add ^ and $ to pattern and make lowercase


// regular Espression Patterns (Brackets):
// [abc] - Matches a single character in the list
// [0-9] - Matches a single character in the range
// (x|y) - Matches x or y


// Metacharacters:
// . - Matches any single character
// \d - Matches a digit
// \D - Matches a non-digit
// \s - Matches a whitespace character
// \S - Matches a non-whitespace character
// \f - Matches a form feed
// \uxxxx - Matches the Unicode character with the hex value xxxx


// Regular Expression Patterns (Braces):
// {x,y} - Matches between x and y occurrences of the preceding pattern
// {x,} - Matches at least x occurrences of the preceding pattern
// {x} - Matches exactly x occurrences of the preceding pattern


// Quantifiers:
// ? - Matches 0 or 1 occurrences of the preceding pattern
// * - Matches 0 or more occurrences of the preceding pattern
// + - Matches 1 or more occurrences of the preceding pattern


// test() - Returns true if the pattern exists in the string:
regex = /\d+/;
result = regex.test("123");
console.log('"test()": ' + result);


// exec() - Returns the first match of the pattern in the string:
regex = /\d+/;
result = regex.exec("The number is 123");
console.log('"exec()": ' + result);

console.log('Found: ' + result[0] +
  '\nIn position: ' + result.index +
  '\nIn string: ' + result.input);

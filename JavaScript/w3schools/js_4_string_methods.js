// slice(start, end)
// The slice() method extracts parts of a string and returns the extracted parts in a new string.
let str = 'Apple, Banana, Kiwi';
let res = str.slice(7, 13);
console.log('Slice():', res);

// substring(start, end)
// The substring() method extracts parts of a string and returns the extracted parts in a new string.
let str2 = 'Apple, Banana, Kiwi';
let res2 = str2.substring(7, 13);
console.log('Substring():', res2);


// Replacing String Content
// replace(searchValue, replaceValue)
// The replace() method replaces a specified value with another value in a string and returns a new string.
let text = 'Please visit Microsoft!';
let newText = text.replace('Microsoft', 'W3Schools');
console.log('Replace():', newText);

// Use regular expressions with the /g flag to replace all occurrences of the string.
let text2 = 'Please visit Microsoft and Microsoft!';
let newText2 = text2.replace(/Microsoft/g, 'W3Schools');
console.log('Replace():', newText2);

// Use a regular expresion with an /i flag to replace all occurrences of the string case-insensitively.
let text3 = 'Please visit Microsoft and Microsoft!';
let newText3 = text3.replace(/MICROSOFT/i, 'W3Schools');
console.log('Replace():', newText3);


// Searching a String
// search(searchValue)
// The search() method searches a string for a specified value and returns the position of the match.
let str3 = 'Please visit Microsoft!';
let n = str3.search('Microsoft');
console.log('Search():', n);


// toUpperCase()
// The toUpperCase() method converts a string to upper case letters.
let str4 = 'Hello World!';
let res4 = str4.toUpperCase();
console.log('toUpperCase():', res4);

// toLowerCase()
// The toLowerCase() method converts a string to lower case letters.
let str5 = 'Hello World!';
let res5 = str5.toLowerCase();
console.log('toLowerCase():', res5);


// trim()
// The trim() method removes whitespace from both sides of a string.
let str6 = '   Hello World!   ';
let res6 = str6.trim();
console.log('trim():', res6);


// The padStart() - Syntax: string.padStart(targetLength, padString)
let str7 = 'Hello';
let res7 = str7.padStart(10,'.');
console.log('padStart():', res7);
// e.g.
let num = 5;
let res8 = num.toString().padStart(10,'0');
console.log('padStart():', res8);

// The padEnd() - Syntax: string.padEnd(targetLength[,padString])
let str8 = 'Hello';
let res9 = str8.padEnd(20,'.');
console.log('padEnd():', res9);
// e.g.
let num2 = 5;
let res10 = num2.toString().padEnd(20,'.');
console.log('padEnd():', res10); // 5..........


// charAt(index)
let text4 = 'Hello World!';
let res11 = text4.charAt(0);
console.log('charAt():', res11); // H

// charCodeAt(index)
let text5 = 'Hello World!';
let res12 = text5.charCodeAt(0);
console.log('charCodeAt():', res12); // 72


// String split() - Syntax: string.split(separator, limit)
let text8 = 'Please visit Microsoft and Microsoft!';
let res15 = text8.split(' ');
console.log('split():', res15); // ["Please", "visit", "Microsoft", "and", "Microsoft!"]


// indexOf(searchValue, fromIndex)
let text6 = 'Please visit Microsoft!';
let res13 = text6.indexOf('o');
console.log('indexOf():', res13); // 4

// lastIndexOf(searchValue, fromIndex)
let text7 = 'Please visit Microsoft!';
let res14 = text7.lastIndexOf('o');
console.log('lastIndexOf():', res14); // 13


// search() - Syntax: str.search(regexp)
let text9 = 'Please visit Microsoft and Microsoft!';
let res16 = text9.search('Microsoft');
console.log('search():', res16); // 13
// e.g. Use search() with regular expressions.
let text10 = 'Please visit Microsoft and Microsoft!';
let res17 = text10.search(/Microsoft/);
console.log('search():', res17); // 13

// match() - Syntax: string.match(regexp)
let text11 = 'The rain in SPAIN stays mainly in the plain!';
let res18 = text11.match(/ain/ig);
console.log('match():', res18); // ["ain", "ain", "ain"]

// includes() - Syntax: string.includes(searchValue, fromIndex)
let text12 = 'Hello world, welcome to the universe!';
let res19 = text12.includes('world');
console.log('includes():', res19); // true

// startsWith() - Syntax: string.startsWith(searchString, position)
let text13 = 'Hello world, welcome to the universe!';
let res20 = text13.startsWith('Hello');
console.log('startsWith():', res20); // true

// endsWith() - Syntax: string.endsWith(searchString, position)
let text14 = 'Hello world, welcome to the universe!';
let res21 = text14.endsWith('universe!');
console.log('endsWith():', res21); // true

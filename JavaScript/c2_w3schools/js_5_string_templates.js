// Template Literals synonyms:

// Template literals
// Template strings
// String templates
// Back-tics Syntax

// Template literals use back-tics (``) to create multi-line strings or define a string:
let text = `He's often called the "father".`;
console.log(text);

// Multiline strings
let text1 =
`The quick
brown fox
jumps over
the lazy dog.`;
console.log(text1);


// String interpolation - Syntax: ${expression}
let fName = "John";
let age = 25;
let sentence = `Hello, my name is ${fName}. I'll be ${age + 1} years old next month.`;
console.log(sentence);

// e.g. Template literals allow expression in the string
let price = 19.95;
let VAT = 0.25;
let total = `Total: ${(price * (1 + VAT)).toFixed(2)}`;
console.log(total); // Total: 24.94


// HTML template literals
// Template literals can be used to create HTML elements:
let header = 'Templates Literals';
let tags = ['template literals', 'javascript', 'web development'];
let html = `<h2>${header}</h2><ul>`;
for (let tag of tags) {
  html += `<li>${tag}</li>`;
}
html += '</ul>';
console.log(html);

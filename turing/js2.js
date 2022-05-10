/**
 * @param {string} str: String to be tested for validity
 * @return {boolean}: Return true if the string si valid else false
 */
// Determine if the imput string is valid, string "s" containing just the characters '(', ')', '{', '}', '[' and ']'. 
var isValid = function(s) {
    // Constraint 1: 1 <= s.length <= 104 
    if (s.length <= 1 || s.length >= 104) {
        return false;
    }
    // Constraint 2: "s" consists of parentheses only '()', '{}', '[]':
    let stack = [];
    let map = { ')': '(', '}': '{', ']': '[' };
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        if (c === '(' || c === '{' || c === '[') {
            stack.push(c);
        } else if (c === ')' || c === '}' || c === ']') {
            if (stack.length === 0 || stack.pop() !== map[c]) {
                return false;
            }
        }
    }
    return stack.length === 0;
};

let s = '{}()[]';

if (isValid(s)) {
    console.log('valid');
} else {
    console.log('invalid');
}

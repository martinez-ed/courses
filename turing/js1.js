/**
 * @param {string[]} ops - List of operations
 * @return {number} - Sum of scores after performing all operations
 */

// keeping score for a baseball game with strange rules.

// List of strings "ops" where "ops[i]" is the "ith" operation must apply to the record and is one of the following:
// "An integer x" - Record a new score of x.
// "+" - Record a new score equal to the sum of the previous two scores, it is guaranteed there will always be at least two previous scores.
// "D" - Record a new score that is the double of the previous score, it is guaranteed there will always be a previous score.
// "C" - Invalidate the previous score, removing it from the record, it is guaranteed there will always be a previous score.

// At the beginning of the game, start with an empty record and return the "sum" of all the scores in the record:
// Example:
// Input: ops = ["5","2","C","D","+"]
// Output: 30

var calPoints = function(ops) {
    var result = null;
    // constraint 1: 1 <= ops.length <= 1000:
    if (ops.length < 1 || ops.length >= 1000) {
        return result;
    }
    var stack = [];
    for (let i = 0; i < ops.length; i++) {
        let op = ops[i];
        // constraint 2: ops[i] is "C" , "D", "+" , or a string represeinting an integer in the range [-3 * 104, 3 * 104]
        if (op !== 'C' && op !== 'D' && op !== '+' && (parseInt(op) < -3 * 104 || parseInt(op) > 3 * 104)) {
            return result;
        }
        // constraint 3: for operation "C" and "D" be at least one previous score on the record
        if (op === 'C' && stack.length !== 0) {
            stack.pop();
        } else if (op === 'D' && stack.length !== 0) {
            stack.push(stack[stack.length - 1] * 2);
        // constraint 4: for operation "+" there will always be at least two previous scores on the record
        } else if (op === '+' && stack.length >= 2) {
            stack.push(stack[stack.length - 1] + stack[stack.length - 2]);
        } else {
            stack.push(parseInt(op));
        }
    }
    result = stack.reduce((a, b) => a + b);
    return result;
};

var ops = ["5","2","C","D","+"];
// var ops = ["5","-2","4","C","D","9","+","+"];
// var ops = ["1"];

console.log(calPoints(ops));

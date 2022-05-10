/**
 * @param TreeNode root
 * @return int
 */
// Given a binary tree, find its maximum depth.
// The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
// Note: A leaf is a node with no children.
// Example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its depth = 3.

function maxDepth(root) { 
    if (root === null) {
        return 0;
    }
    var maxDepth = 0;
    var stack = [];
    stack.push(root);
    while (stack.length !== 0) {
        var node = stack.pop();
        if (node.left !== null) {
            stack.push(node.left);
        }
        if (node.right !== null) {
            stack.push(node.right);
        }
        if (node.left === null && node.right === null) {
            maxDepth++;
        }
    }
    return maxDepth;
}

// x = maxDepth('3,9,20,null,null,15,7');
// console.log(x);

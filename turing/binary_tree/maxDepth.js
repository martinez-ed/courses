/**
 * @param TreeNode root
 * @return int
 * 
 * Given a binary tree, find its maximum depth.
 * The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
 * Note: A leaf is a node with no children.
 */
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

// e.g. binary tree [5,3,6,2,4,null,null,null,1]
//     5
//    / \
//   3   6
//  / \
// 2   4
//    /
//   1
// return its depth = 3.

// e.g. 1) binary tree [3,9,20,null,null,15,7]
//   3
//  / \
// 9  20
//  \  \
// 15   7
// return its depth = 3.

// e.g. 2) binary tree [7,3,15,null,null,9,20,3,2,4,null,null,5,null,null,6,19,18,null,null,17]
//     7
//  /   \
// 3     15
//  \   /  \
//   9 20    3
//  /  \   / \
// 2   4 5   6
//  \
//  19  18
//  \
//  17
// return its depth = 5.
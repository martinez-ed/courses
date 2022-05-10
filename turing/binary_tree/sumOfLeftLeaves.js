/**
 * Definition for a binary tree node:
 * function TreeNode(val, left, right) {
 *   this.val = (val===undefined ? 0 : val)
 *   this.left = (left===undefined ? null : left)
 *   this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
class TreeNode {
  constructor(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
  }
}

// function sumOfLeftLeaves(root) {
//   if (!root) return 0;
//   let sum = 0;
//   if (root.left && !root.left.left && !root.left.right) {
//     sum += root.left.val;
//   }
//   sum += sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
//   return sum;
// };

var sumOfLeftLeaves = function(root) {
  if (!root) return 0;
  if (root.left && !root.left.left && !root.left.right) return root.left.val + sumOfLeftLeaves(root.right);
  return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
};

//e.g. 1) [3,9,20,null,null,15,7], return 24
// diagram:
//     3
//    / \
//   9  20
//     /  \
//    15   7
x = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
console.log('Sum of left leaves: ' + sumOfLeftLeaves(x));

//e.g. 2) Binary tree: [5,3,6,2,4,null,null,null,1], return: 9
// diagram:
//       5
//     /   \
//    3     6
//   / \   / \
//  2   4 1   null
// /
// 1
x = new TreeNode(5, new TreeNode(3, new TreeNode(2), new TreeNode(4, new TreeNode(1), null)), new TreeNode(6)); // return 9
console.log('Sum of left leaves: ' + sumOfLeftLeaves(x));

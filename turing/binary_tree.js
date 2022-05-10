// Binary tree syntax:
//     3
//    / \
//   9  20
//     /  \
//    15   7
//
class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }

    addLeft(val) {
        this.left = new TreeNode(val);
        return this.left;
    }

    addRight(val) {
        this.right = new TreeNode(val);
        return this.right;
    }
}

function createTree(arr) {
    var root = new TreeNode(arr[0]);
    var stack = [];
    stack.push(root);
    for (var i = 1; i < arr.length; i++) {
        var node = stack.pop();
        if (arr[i] !== null) {
            node.addLeft(arr[i]);
            stack.push(node.left);
        }
        i++;
        if (arr[i] !== null) {
            node.addRight(arr[i]);
            stack.push(node.right);
        }
    }
    return root;
}

function printTree(root) {
    if (root === null) {
        return;
    }
    var stack = [];
    stack.push(root);
    while (stack.length !== 0) {
        var node = stack.pop();
        console.log(node.val);
        if (node.left !== null) {
            stack.push(node.left);
        }
        if (node.right !== null) {
            stack.push(node.right);
        }
    }
}

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


function sumLeftLeaves(root) {
    if (root === null) {
        return 0;
    }
    var sum = 0;
    var stack = [];
    stack.push(root);
    while (stack.length !== 0) {
        var node = stack.pop();
        if (node.left !== null) {
            if (node.left.left === null && node.left.right === null) {
                sum += node.left.val;
            } else {
                stack.push(node.left);
            }
        }
        if (node.right !== null) {
            stack.push(node.right);
        }
    }
    return sum;
}

function sumRightLeaves(root) {
    if (root === null) {
        return 0;
    }
    var sum = 0;
    var stack = [];
    stack.push(root);
    while (stack.length !== 0) {
        var node = stack.pop();
        if (node.right !== null) {
            if (node.right.left === null && node.right.right === null) {
                sum += node.right.val;
            } else {
                stack.push(node.right);
            }
        }
        if (node.left !== null) {
            stack.push(node.left);
        }
    }
    return sum;
}

x = sumLeftLeaves(createTree([3,9,20,null,null,15,7]));
console.log('Sum of left leaves: ' + x);2

y = maxDepth(createTree([3,9,20,null,null,15,7]));
// y = maxDepth(createTree([5,3,6,2,4,null,null,null,1]));
// y = maxDepth(createTree([7,3,15,null,null,9,20,3,2,4,null,null,5,null,null,6,19,18,null,null,17]));
console.log('maxDepth: ' + y);

z = sumRightLeaves(createTree([3,9,20,null,null,15,7]));
console.log('Sum of right leaves: ' + z);

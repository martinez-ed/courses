# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

class Solution(object):
  def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
      return 0
    sum = 0
    if root.left and not root.left.left and not root.left.right:
      sum += root.left.value
    sum += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    return sum

#Input: root = [3,9,20,null,null,15,7]
#Output: 24
#Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
#diagram:
#     3
#    / \
#   9  20
#     /  \
#    15   7
x = TreeNode(3)
x.left = TreeNode(9)
x.right = TreeNode(20)
x.right.left = TreeNode(15)
x.right.right = TreeNode(7)
print(Solution().sumOfLeftLeaves(x))

#Input: root = [5,3,6,2,4,null,null,1]
#Output: 6
#Explanation: There are three left leaves in the binary tree, with values 3, 2 and 1 respectively. Return 6.
#diagram:
#        5
#       / \
#      3   6
#     / \
#    2   4
#       /
#      1
x = TreeNode(5)
x.left = TreeNode(3)
x.right = TreeNode(6)
x.left.left = TreeNode(2)
x.left.right = TreeNode(4)
x.left.right.left = TreeNode(1)
print(Solution().sumOfLeftLeaves(x))

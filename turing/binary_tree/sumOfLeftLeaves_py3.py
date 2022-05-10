# Definition for a binary tree node.
from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if root is None:
      return 0
    ans = 0
    if root.left and not root.left.left and not root.left.right:
      ans += root.left.val
    ans += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    return ans

x = TreeNode(3)
x.left = TreeNode(9)
x.right = TreeNode(20)
x.right.left = TreeNode(15)
x.right.right = TreeNode(7)
print(Solution().sumOfLeftLeaves(x))

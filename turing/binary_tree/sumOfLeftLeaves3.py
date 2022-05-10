# binary tree:
#          6
#         / \
#       (5)  8
#       /   / \
#     (3) (4)  9
#     / \     /
#   (1)  7  (2)

# Definition of a class:
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Buinding a tree:
my_tree = \
  TreeNode \
    ( 6
    , TreeNode
        ( 5
        , TreeNode(3, TreeNode(1), TreeNode(7))
        , None
        )
    , TreeNode
        ( 8
        , TreeNode(4)
        , TreeNode(9, TreeNode(2), None)
        )
    )

# Definition of a class for the solution:
# class Solution:
#   def sumOfLeftLeaves(t, is_left=False):
#     if not t:
#       return 0
#     elif is_left:
#       return t.val + Solution.sumOfLeftLeaves(t.left, True) + Solution.sumOfLeftLeaves(t.right, False)
#     else:
#       return 0 + Solution.sumOfLeftLeaves(t.left, True) + Solution.sumOfLeftLeaves(t.right, False)

# print(Solution().sumOfLeftLeaves(my_tree))


# Recursive solution:
def sum_left (t, is_left=False):
  if not t:
    return 0
  elif is_left:
    return t.val + sum_left(t.left, True) + sum_left(t.right, False)
  else:
    return 0 + sum_left(t.left, True) + sum_left(t.right, False)

print(sum_left(my_tree)) # 15


# Another option is use mutual recursion:
def sum_left (t):
  if not t:
    return 0
  else:
    return t.val + sum_left(t.left) + sum_right(t.right)

def sum_right (t):
  if not t:
    return 0
  else:
    return sum_left(t.left) + sum_right(t.right)

print(sum_left(my_tree)) # 21 - root will sum
print(sum_right(my_tree)) # 15

class Tree(object):
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

# sumLeftLeaves = g = lambda t, f=0: t and f*t.value(t.left==t.right) + g(t.left, 1) + g(t.right) or 0

def g(t, f=0): # "t" is a Tree object and "f" is a flag
  if t is not None:
    sum_left_leaves = g(t.left, 1)
    return (f*t.value) + sum_left_leaves
  return 0

# e.g. 1)
#        1
#       / \
#      3   2
#     / \
#    4   5
parent = Tree(1)
broter = Tree(2)
me = Tree(3)
child1 = Tree(4)
child2 = Tree(5)
# set connections
parent.left = me
parent.right = broter
me.left = child1
me.right = child2
print(g(parent)) #7
print(g(parent, 1)) #8 - include the root

# e.g. 2)
#        3
#       / \
#      9   20
#         /  \
#        15   7
parent = Tree(3)
broter = Tree(20)
me = Tree(9)
child1 = Tree(15)
child2 = Tree(7)
# set connections
parent.left = me
parent.right = broter
me.left = child1
me.right = child2
print(g(parent)) #24

# e.g. 3)
#        5
#       / \
#      3   6
#     / \
#    2   4
#       /
#      1
parent = Tree(5)
broter = Tree(6)
me = Tree(3)
child1 = Tree(2)
child2 = Tree(4)
child3 = Tree(1)
# set connections
parent.left = me
parent.right = broter
me.left = child1
me.right = child2
me.left.left = child3
print(g(parent)) #6
print(g(parent, 1)) # include the root node, return 11

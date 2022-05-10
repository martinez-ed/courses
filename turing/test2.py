# Given a binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root is None:
#             return 0
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
#
# if __name__ == "__main__":
#     line = input()
#     root = TreeNode(int(line))
#     line = input()
#     root.left = TreeNode(int(line))
#     line = input()
#     root.right = TreeNode(int(line))
#     line = input()
#     root.left.left = TreeNode(int(line))
#     line = input()
#     root.left.right = TreeNode(int(line))
#     line = input()
#     root.right.left = TreeNode(int(line))
#     line = input()
#     root.right.right = TreeNode(int(line))
#     print(Solution().maxDepth(root))
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

if __name__ == "__main__":
    line = input()
    root = TreeNode(int(line))
    line = input()
    root.left = TreeNode(int(line))
    line = input()
    root.right = TreeNode(int(line))
    line = input()
    root.left.left = TreeNode(int(line))
    line = input()
    root.left.right = TreeNode(int(line))
    line = input()
    root.right.left = TreeNode(int(line))
    line = input()
    root.right.right = TreeNode(int(line))
    print(Solution().maxDepth(root))

result = Solution().maxDepth('[3,9,20,null,null,15,7]')
print(result)

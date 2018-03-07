# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#         sum = [0] # 44ms
#         def recursion(node, sum, isLeft):
#             if node:
#                 if isLeft and not node.left and not node.right: sum[0] += node.val
#                 recursion(node.left, sum, True)
#                 recursion(node.right, sum, False)
                
#         recursion(root, sum, False)
#         return sum[0]

        if not root: # 48ms
            return 0
        else:
            if root.left and not root.left.left and not root.left.right:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = []
        def recursion(node):
            if node:
                recursion(node.left)
                values.append(node.val)
                recursion(node.right)
        def difference(values):
            return abs(values[0] - values[1])
        recursion(root)
        return min(map(difference, zip(values[:-1], values[1:])))

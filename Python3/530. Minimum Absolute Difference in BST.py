# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = [] # 120ms 将二叉树转化为了有序数组
        def Tree2List(node, values):
            if node:
                Tree2List(node.left, values)
                values.append(node.val)
                Tree2List(node.right, values)
        Tree2List(root, values)
        return min([abs(x-y) for x, y in zip(values[:-1], values[1:])])            

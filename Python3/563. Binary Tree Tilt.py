# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # def recursion(node): # 83ms
        #     if not node: return (0, 0)
        #     left = recursion(node.left)
        #     right = recursion(node.right)
        #     return (left[0] + right[0] + node.val, abs(left[0] - right[0]) + left[1] + right[1])
        # return recursion(root)[1]
        
        def recursion(node): # 84ms
            if not node: return 0
            left = recursion(node.left)
            right = recursion(node.right)
            self.tilt += abs(left - right)
            return node.val + left + right
        self.tilt = 0
        recursion(root)
        return self.tilt

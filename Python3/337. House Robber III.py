# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # def recursion(node, isrobbed): # 方法是正确的, 但是超时了
        #     if node:
        #         if not node.left and not node.right:
        #             return node.val if not isrobbed else 0
        #         if isrobbed:
        #             return recursion(node.left, False) + recursion(node.right, False)
        #         else:
        #             return max(node.val + recursion(node.left, True) + recursion(node.right, True), 
        #                       recursion(node.left, False) + recursion(node.right, False))
        #     else:
        #         return 0
        # return recursion(root, False)
        
        # dp = {} # 动态规划, 通过了, 80ms
        # def recursion(node, isrobbed):
        #     if (node, isrobbed) in dp:
        #         return dp[(node, isrobbed)]
        #     if node:
        #         if not node.left and not node.right:
        #             dp[(node, isrobbed)] = node.val if not isrobbed else 0
        #             return dp[(node, isrobbed)]
        #         if isrobbed:
        #             dp[(node, isrobbed)] = recursion(node.left, False) + recursion(node.right, False)
        #             return dp[(node, isrobbed)]
        #         else:
        #             dp[(node, isrobbed)] = max(node.val + recursion(node.left, True) + recursion(node.right, True), 
        #                                         recursion(node.left, False) + recursion(node.right, False))
        #             return dp[(node, isrobbed)]
        #     else:
        #         return 0
        # return recursion(root, False)
        
        def dfs(node): # 64ms 更快, 更直观
            if not node:
                return (0, 0)
            la, lb = dfs(node.left)
            ra, rb = dfs(node.right)
            a = node.val + lb + rb
            b = max(la, lb) + max(ra, rb)
            return (a, b)
        a, b = dfs(root)
        return max(a, b)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # # recursive # 36ms
        # ans = []
        # def recursion(node):
        #     if node:
        #         recursion(node.left)
        #         ans.append(node.val)
        #         recursion(node.right)
        # recursion(root)
        # return ans
        
        if not root: # 40ms
            return []
        stack = [(root, False)]
        ans = []
        while len(stack) > 0:
            node, visited = stack.pop()
            if visited:
                ans.append(node.val)
                if node.right:
                    stack.append((node.right, False))
            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        def recursion(node):
            if not node.left and not node.right:
                if node.val == 1:
                    return False
                else:
                    return True
            else:
                if node.left:
                    left = recursion(node.left)
                    if left:
                        node.left = None
                if node.right:
                    right = recursion(node.right)
                    if right:
                        node.right = None
                if node.left or node.right:
                    return False
                else:
                    return node.val == 0
        ans = recursion(root)
        if ans:
            return []
        return root

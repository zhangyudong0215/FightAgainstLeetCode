# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
#         def reverse(node):
#             if node:
#                 if node.left and node.right:
#                     node.left, node.right = node.right, node.left
#                 elif node.left:
#                     node.right = node.left
#                     node.left = None
#                 elif node.right:
#                     node.left = node.right
#                     node.right = None

#                 if node.left:
#                     node.left = reverse(node.left)
#                 if node.right:
#                     node.right = reverse(node.right)
#                 return node
#             else:
#                 return None
        
#         return reverse(root)
        
        def reverse(node):
            if not node:
                return None
            
            left = reverse(node.left)
            right = reverse(node.right)
            
            node.right = left
            node.left = right
            
            return node
        
        return reverse(root)

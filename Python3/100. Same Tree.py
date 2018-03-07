# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # def recursion(node1, node2): # 40ms
        #     if not node1 and not node2:
        #         return True
        #     elif node1 and not node2:
        #         return False
        #     elif not node1 and node2:
        #         return False
        #     else:
        #         if node1.val != node2.val:
        #             return False
        #         else:
        #             return recursion(node1.left, node2.left) and recursion(node1.right, node2.right)
        # return recursion(p, q)

        if not p and not q: # 44ms
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

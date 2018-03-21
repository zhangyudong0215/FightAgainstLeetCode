# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return [] # 68ms
        currlevel = [root]
        nextlevel = []
        ans = []
        while len(currlevel) > 0:
            maxvalue = currlevel[0].val
            while len(currlevel) > 0:
                node = currlevel.pop()
                if node.val > maxvalue:
                    maxvalue = node.val
                if node.left: nextlevel.append(node.left)
                if node.right: nextlevel.append(node.right)
            ans.append(maxvalue)
            currlevel = nextlevel
            nextlevel = []
        return ans

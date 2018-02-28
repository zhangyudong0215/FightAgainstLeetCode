# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         else:
#             return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution:
    def maxDepth(self, root): # stack 解决方案
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        tstack, depth = [root], 0

        while tstack:
            nextlevel = []
            while tstack:
                top = tstack.pop()
                if top.left:
                    nextlevel.append(top.left)
                if top.right:
                    nextlevel.append(top.right)
            tstack = nextlevel
            depth += 1
        return depth

class Solution:
    def maxDepth(self, root): # deque 解决方案
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        tdeque, depth = collections.deque(), 0
        tdeque.append(root)
        while tdeque:
            nextlevel = collections.deque()
            while tdeque:
                front = tdeque.popleft()
                if front.left:
                    nextlevel.append(front.left)
                if front.right:
                    nextlevel.append(front.right)
            tdeque = nextlevel
            depth += 1
        return depth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def findBottomLeftValue(self, root): # 每次突破最底层的时候就更新ans # 56ms
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     ans = [-1, 0]
    #     def recursion(node, depth, ans):
    #         if node:
    #             recursion(node.left, depth+1, ans)
    #             if depth > ans[0]:
    #                 ans[0], ans[1] = depth, node.val
    #             recursion(node.right, depth+1, ans)        
    #     recursion(root, 0, ans)
    #     return ans[1]
        
    def findBottomLeftValue(self, root): # 从右开始的广度搜索, 最后一个就是目标node # 68ms
        """
        :type root: TreeNode
        :rtype: int
        """
        self.queue = collections.deque([])
        self.queue.append(root)
        return self.bfs()

    def bfs(self):
        while len(self.queue):
            node = self.queue.popleft()
            if node.right:
                self.queue.append(node.right)
            if node.left:
                self.queue.append(node.left)
        return node.val

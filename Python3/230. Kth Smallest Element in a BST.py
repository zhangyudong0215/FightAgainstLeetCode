# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # nums = [] # 得到的是全体升序数据, 会浪费很多时间和空间
        # def recursion(node):
        #     if node:
        #         recursion(node.left)
        #         nums.append(node.val)
        #         recursion(node.right)
        # recursion(root)
        # return nums[k-1]
        
        # ram = [0, 0] # 这种方法将空间复杂度降到O(1)
        # def recursion(node):
        #     if node:
        #         recursion(node.left)
        #         ram[1] += 1
        #         if ram[1] == k:
        #             ram[0] = node.val
        #             return # 这里的return应该只能结束一个局部的递归, 和它并列的递归依然存在
        #         recursion(node.right)
        # recursion(root)
        # return ram[0]
        
        stack = [] # 时间复杂度最小, 空间复杂度也比较低
        order = 0
        while len(stack) > 0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                order += 1
                if order == k:
                    return root.val
                root = root.right
'''
另外, 题目中的 Follow up: {
    What if the BST is modified (insert/delete operations) 
    often and you need to find the kth smallest frequently? 
    How would you optimize the kthSmallest routine?
}
如果进行高频的插入和删除, 那么该怎么优化?
(不一定准确): 重新构造整个树, 在节点中新增一个属性, 代表此节点作为根节点的子树的节点总数, 
            insert和delete方法在修改的时候同时也要修改这个值, 
            如此, 利用这个数据, 查询就会变得比较容易. 
'''

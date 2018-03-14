# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # if len(nums) == 0: # 209ms 递归
        #     return None
        # elif len(nums) == 1:
        #     return TreeNode(nums[0])
        # else:
        #     index = nums.index(max(nums))
        #     node = TreeNode(nums[index])
        #     node.left = self.constructMaximumBinaryTree(nums[: index])
        #     node.right = self.constructMaximumBinaryTree(nums[index+1: ])
        #     return node

        if not nums: # 173ms 栈
            return None
        stack = []
        for num in nums:
            curr = TreeNode(num)
            while stack and stack[-1].val < num:
                curr.left = stack[-1]
                stack.pop()
            if stack:
                stack[-1].right = curr
            stack.append(curr)
        return stack[0]

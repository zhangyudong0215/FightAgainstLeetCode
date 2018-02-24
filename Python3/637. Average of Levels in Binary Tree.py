# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nums = []
        counts = []
        self.dealNode(root, 0, nums, counts)
        return [x/float(y) for (x, y) in zip(nums, counts)]
    
    def dealNode(self, node, layer, nums, counts):
        if node:
            if layer < len(nums):
                nums[layer] += node.val
                counts[layer] += 1
            else:
                nums.append(node.val)
                counts.append(1)
            self.dealNode(node.left, layer+1, nums, counts)
            self.dealNode(node.right, layer+1, nums, counts)

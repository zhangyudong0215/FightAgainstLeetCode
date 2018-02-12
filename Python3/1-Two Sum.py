class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i+1:]):
                if num_i == target-num_j:
                    return [i, j+i+1]

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sum(nums) - min(nums)*len(nums) # 96ms
        
        length = len(nums) # 68ms
        count = 0
        min_num = nums[0]
        for num in nums:
            count += num
            if num < min_num:
                min_num = num
        return count - min_num * length

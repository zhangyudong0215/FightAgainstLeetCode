class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # count = nums.count(0) # 56ms
        # index = 0
        # for num in nums:
        #     if num:
        #         nums[index] = num
        #         index += 1
        # while index < len(nums):
        #     nums[index] = 0
        #     index += 1
        
        position = 0 # 52ms 没有显著改善
        for index, num in enumerate(nums):
            if num:
                nums[position], nums[index] = nums[index], nums[position]
                position += 1

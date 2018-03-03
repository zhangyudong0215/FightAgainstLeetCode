class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for num in nums: # 220ms
        #     index = abs(num) - 1
        #     nums[index] = -abs(nums[index])
        # return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
        for i in range(len(nums)): # 252ms
            while nums[i] != nums[nums[i]-1]:
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] # 是错误的
                temp = nums[i]
                nums[i] = nums[temp-1]
                nums[temp-1] = temp      
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans

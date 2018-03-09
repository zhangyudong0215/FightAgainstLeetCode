class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # numsDict = {} # 140ms
        # for num in nums:
        #     numsDict[num] = numsDict.get(num, 0) + 1
        # for num in numsDict:
        #     if numsDict[num] > 1:
        #         return True
        # return False
        
        # numsDict = collections.Counter(nums) # 56ms
        # for value in numsDict.values():
        #     if value > 1:
        #         return True
        # return False
        
        return len(nums) != len(set(nums)) # 52ms

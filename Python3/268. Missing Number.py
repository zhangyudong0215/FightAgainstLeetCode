class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = max(nums)
        missing =  list(set(range(maxnum+1)) - set(nums))
        if len(missing) > 0:
            return missing[0]
        else:
            return maxnum + 1

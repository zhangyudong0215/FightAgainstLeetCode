class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = [[], [nums[0]]]
        for i in range(1, len(nums)):
            temp = []
            for item in ans:
                temp.append(item + [nums[i]])
            ans.extend(temp)
        return ans

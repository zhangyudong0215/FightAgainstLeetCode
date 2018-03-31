class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0 # 80ms O(n)而且空间复杂度为O(1)
        for index in range(len(nums)):
            if nums[index] >= 0:
                count = 0
                tag = index
                while nums[tag] >= 0:
                    count += 1
                    temp = nums[tag]
                    nums[tag] = -1
                    tag = temp
                ans = max(ans, count)
            index += 1
        return ans

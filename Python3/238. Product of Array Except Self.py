class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 不能用除法, O(n)时间复杂度, 除了output外的O(1)空间复杂度
        length = len(nums)
        ans = [1 for _ in range(length)]
        pi = pj = 1
        for i in range(length):
            j = -i - 1
            ans[i] *= pi
            pi *= nums[i]
            ans[j] *= pj
            pj *= nums[j]
        return ans

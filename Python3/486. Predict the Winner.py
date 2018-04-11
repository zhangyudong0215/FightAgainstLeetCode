class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        length = len(nums) # 独立完成了一次dp问题
        if length == 1:
            return True
        dp = {}
        def recursion(start, end):
            if end == start + 1:
                if nums[start] > nums[end]:
                    dp[(start, end)] = (nums[start], nums[end])
                else:
                    dp[(start, end)] = (nums[end], nums[start])
                return dp[(start, end)]
            if (start, end) in dp:
                return dp[(start, end)]
            min1, max1 = recursion(start+1, end)
            max1 += nums[start]
            min2, max2 = recursion(start, end-1)
            max2 += nums[end]
            if max1 > max2:
                dp[(start, end)] = (max1, min1)
            else:
                dp[(start, end)] = (max2, min2)
            return dp[(start, end)]
        a, b = recursion(0, length-1)
        return a >= b

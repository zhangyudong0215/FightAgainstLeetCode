class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = sorted(nums) # 108ms
        # min1, min2, max1, max2, max3 = nums[0], nums[1], nums[-1], nums[-2], nums[-3]
        # return max(min1*min2*max1, max1*max2*max3)
        
        num3 = sorted(nums[:3])
        min1 = min2 = num3[1]
        max3 = max2 = max1 = num3[0]
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            else:
                pass

            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
            else:
                pass
        return max(min1*min2*max1, max1*max2*max3)

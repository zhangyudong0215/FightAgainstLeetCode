class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # length = len(nums) # 超时
        # if not length:
        #     return []
        # maxnum = max(nums)
        # nums *= 2
        # for i in range(length):
        #     if nums[i] < maxnum:
        #         for j in range(i+1, i+length):
        #             if nums[j] > nums[i]:
        #                 nums[i] = nums[j]
        #                 break
        #     else:
        #         nums[i] = -1
        # return nums[: length]
        
        length = len(nums) # stack 208ms
        if not length:
            return []
        nums *= 2
        stack = []
        for i in range(2*length-1, -1, -1):
            while stack and nums[i] >= stack[-1][1]:
                stack.pop()
            if stack:
                temp = stack[-1][1]
                stack.append((i, nums[i]))
                nums[i] = temp
            else:
                stack.append((i, nums[i]))
                nums[i] = -1
        return nums[: length]

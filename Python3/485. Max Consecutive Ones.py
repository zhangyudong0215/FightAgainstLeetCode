class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_length = 0 # 92ms
        # length = 0
        # while nums:
        #     num = nums.pop()
        #     if num:
        #         length += 1
        #     else:
        #         length = 0
        #     if length > max_length:
        #         max_length = length
        # return max_length
        
#         length = 0 # 76ms
#         max_length = 0       
#         for num in nums:
#             if num == 1:
#                 length += 1
#             else:
#                 max_length = max(max_length, length)
#                 length = 0
#         return max(max_length, length)
        
        s = ''.join(map(str, nums)) # 100ms
        s = s.split('0')
        return max(map(len, s))

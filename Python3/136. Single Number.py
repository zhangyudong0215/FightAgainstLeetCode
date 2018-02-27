class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashtable = {}
        # for num in nums:
        #     if num in hashtable:
        #         del hashtable[num]
        #     else:
        #         hashtable[num] = True
        # return list(hashtable.keys())[0]
        
        ans = 0
        for num in nums:
            ans ^= num # a^b^c^b^c = a 这种方法简洁，但是速度慢
        return ans

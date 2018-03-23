class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        XOR = 0 # 52ms
        for num in nums:
            XOR ^= num # 得到的是a和b的XOR(异或)
        diff = XOR & -XOR # 找到a和b的XOR二进制表示中最后一个1, 意味着这是a和b的二进制表示中最后一个不同的bit, 依次把a和b分开了, 精彩至极
        a, b = 0, 0
        for num in nums:
            if diff & num:
                a ^= num
            else:
                b ^= num
        return [a, b]

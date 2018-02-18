class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # count = 0 # 本人拙劣的解法
        # res = num
        # while res:
        #     res //= 2
        #     count += 1
        # return 2**count-1-num
        
        mask = ~0 # 位运算，速度比上面这个快4ms (36ms vs 40ms)
        while mask & num:
            mask <<= 1
        return ~mask & ~num

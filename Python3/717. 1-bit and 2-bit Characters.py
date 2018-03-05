class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        # index = 0 # 这些字符串都是有0或10或11组成的 # 52ms
        # while index < len(bits)-1:
        #     index += bits[index]+1
        # return index == len(bits)-1
        
        # index = -2 # 44ms
        # if len(bits) == 1 or bits[index] == 0: return True
        # count = 0
        # while abs(index) <= len(bits) and bits[index] == 1:
        #     count += 1
        #     index -= 1
        # if count%2:
        #     return False
        # else:
        #     return True
        
        # 上面的方法换了一种写法 # 60ms 还慢了
        index = len(bits) - 2
        if len(bits) == 1 or bits[index] == 0: return True
        count = 0
        while index >= 0 and bits[index] == 1:
            count += 1
            index -= 1
        return False if count%2 == 1 else True

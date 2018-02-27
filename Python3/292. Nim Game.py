class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # def IWin(n): # 递归超时
        #     if n == 4:
        #         return False
        #     elif n < 4:
        #         return True
        #     else:
        #         return IWin(n-1) or IWin(n-2) or IWin(n-3)
        # return IWin(n)
        return n % 4 != 0

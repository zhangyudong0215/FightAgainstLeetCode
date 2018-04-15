class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0 # 这很数学
        d = 2
        while n > 1:
            while n%d == 0:
                ans += d
                n //= d
            d += 1
        return ans

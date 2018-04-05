class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1] * (n+1)
        for i in range(2, n+1):
            ans[i] = ans[i-1]
            for j in range(1, 10):
                if i-j > 0 and ans[i-j] * j > ans[i]:
                    ans[i] = ans[i-j] * j
                if i < n: # 关键是这一步, 如果不等于和, 那么可以不拆分
                    ans[i] = max(ans[i], i)
        return ans[n]

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # pairs = sorted(pairs, key=lambda x: x[0]) # 动态规划, 居然也超时了
        # dp = [1] * len(pairs)
        # for i in range(len(pairs)):
        #     for j in range(i):
        #         if pairs[j][1] < pairs[i][0]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
        
        pairs.sort(key=lambda x: x[1])
        cur = pairs[0][0] - 1
        ans = 0
        for a, b in pairs:
            if cur < a:
                cur = b
                ans += 1
        return ans

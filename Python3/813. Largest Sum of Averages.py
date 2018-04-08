class Solution:
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        # def recursion(array, k): # 超时, 但是逻辑应该是对的
        #     if k == 1:
        #         return sum(array)/len(array)
        #     ans = 0
        #     for i in range(1, len(array)-k+2):
        #         total = sum(array[: i])/float(i) + recursion(array[i: ], k-1)
        #         ans = max(total, ans)
        #     return ans
        # return recursion(A, K)

        dp = {}
        def search(n, k):
            if (n, k) in dp:
                return dp[n, k]
            if k == 1:
                dp[n, k] = sum(A[: n]) / n
                return dp[n, k]
            dp[n, k], cur = 0, 0
            for i in range(n-1, 0, -1):
                cur += A[i]
                dp[n, k] = max(dp[n, k], search(i, k-1) + cur/(n-i))
            return dp[n, k]
        return search(len(A), K)

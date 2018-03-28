class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        # ans = list(range(1, n+1)) # 828ms 效率极低
        # for i in range(1, k):
        #     ans = ans[: i] + ans[i:][::-1]
        # return ans
        
        ans = list(range(1, n-k+1)) # 68ms
        i, j = n, n-k+1
        while i >= j:
            if i >= j:
                ans.append(i)
                i -= 1
            if i >= j:
                ans.append(j)
                j += 1
        return ans

class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # ans = 0 # 原创解法
        # i = 0
        # while i < len(arr):
        #     j = arr[i]
        #     k = i
        #     while k <= j:
        #         if arr[k] > j:
        #             j = arr[k]
        #         k += 1
        #     ans += 1
        #     i = j + 1
        # return ans
        
        # discuss中的有意思的解法, 累计和
        ans = 0
        sum1 = sum2 = 0
        for i, num in enumerate(arr):
            sum1 += i
            sum2 += num
            if sum1 == sum2:
                ans += 1
        return ans

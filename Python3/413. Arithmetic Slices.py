class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # start = 0 # 44ms 思路正确但是执行太繁琐
        # length = len(A)
        # ans = 0
        # def maxLength(start):
        #     n = 2
        #     end = start + 1
        #     d = A[end] - A[start]
        #     while end < length-1 and (A[end+1] - A[end]) == d:
        #         n += 1
        #         end += 1
        #     return n, end    
        # while start <= length - 3:
        #     n, start = maxLength(start)
        #     ans += (n - 1)*(n - 2)/2
        # return int(ans)

        length = len(A) # 44ms
        if length < 3:
            return 0
        count = 0
        ans = 0
        for i in range(1, length-1):
            if (A[i-1] - A[i]) == (A[i] - A[i+1]):
                count += 1
            else:
                ans += count*(count+1)//2
                count = 0
        ans += count*(count+1)//2
        return ans

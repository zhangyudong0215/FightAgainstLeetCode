class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = {} # 无穷无尽的超时
        A.sort()
        numsDict = {}
        for i in range(len(A)):
            for j in range(i, len(A)):
                product = A[i]*A[j]
                k = j + 1
                while k < len(A) and A[k] < product:
                    k += 1
                if k < len(A) and A[k] == product:
                    if product in numsDict:
                        numsDict[product].append((A[i], A[j]))
                    else:
                        numsDict[product] = [(A[i], A[j])]
                # if product in A[j+1: ]:
                #     if product in numsDict:
                #         numsDict[product].append((A[i], A[j]))
                #     else:
                #         numsDict[product] = [(A[i], A[j])]
        def recursion(num):
            if num in dp:
                return dp[num]
            if num not in numsDict:
                dp[num] = 1
            else:
                count = 1
                for pair in numsDict[num]:
                    if pair[0] == pair[1]:
                        count += recursion(pair[0]) * recursion(pair[1])
                    else:
                        count += 2 * recursion(pair[0]) * recursion(pair[1])
                dp[num] = count
            return dp[num]
        ans = 0
        for root in A:
            ans += recursion(root)
        return ans % (10 ** 9 + 7)

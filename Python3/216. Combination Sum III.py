class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def recursion(k, n, cap): # 递归
            if not k:
                return [[]] * (not n)
            return [comb + [last] for last in range(1, cap) for comb in recursion(k-1, n-last, last)]
        return recursion(k, n, 10)        

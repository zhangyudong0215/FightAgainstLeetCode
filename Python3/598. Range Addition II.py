class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        op1 = (x[0] for x in ops)
        op2 = (x[1] for x in ops)
        return min(op1) * min(op2)

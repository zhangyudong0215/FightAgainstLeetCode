class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def recursion(s='', left=0, right=0):
            if len(s) == 2*n:
                ans.append(s)
            if left < n:
                recursion(s+'(', left+1, right)
            if left > right:
                recursion(s+')', left, right+1)
        recursion('')
        return ans

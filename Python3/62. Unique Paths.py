class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n - 2
        y = m - 1
        def c(total, y):
            a = 1
            b = 1
            while y > 0:
                a *= total
                b *= y
                total -= 1
                y -= 1
            return a/b
        return c(total, y)

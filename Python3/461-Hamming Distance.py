class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        total = 0
        while x or y:
            num_x = x % 2
            num_y = y % 2
            if num_x != num_y:
                total += 1
            x //= 2
            y //= 2
        return total

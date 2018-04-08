class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ans = 0
        length = len(points)
        for i in range(length):
            x1, y1 = points[i]
            for j in range(length):
                x2, y2 = points[j]
                for k in range(length):
                    x3, y3 = points[k]
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) * 0.5
                    ans = max(ans, area)
        return ans

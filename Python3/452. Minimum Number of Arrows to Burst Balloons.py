class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # points.sort(key=lambda x: x[1])
        # ans, end = 0, -float('inf')
        # for point in points:
        #     if point[0] > end:
        #         ans += 1
        #         end = point[1]
        # return ans
        
        # 实现discuss中的此问题模板做法
        points.sort(key=lambda x: x[0])
        ans, end = 0, -float('inf')
        for point in points:
            if point[0] > end:
                ans += 1
                end = point[1]
            else:
                end = min(end, point[1])
        return ans

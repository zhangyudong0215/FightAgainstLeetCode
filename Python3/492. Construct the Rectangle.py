class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = math.floor(math.sqrt(area))
        while area%W:
            W -= 1
        return [int(area/W), W]

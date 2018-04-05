class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edges = collections.defaultdict(int)
        length = sum(wall[0])
        for row in wall:
            total = 0
            for brick in row:
                total += brick
                if total < length:
                    edges[total] += 1
        if not edges:
            return len(wall)
        return len(wall) - max(edges.values())

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from functools import partial # 1428ms
        def distance(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2
        total = 0
        for point in points:
            getDistance = partial(distance, point)
            distances = map(getDistance, points)
            distanceDict = collections.Counter(distances)
            selfcount = distanceDict[0]
            total -= selfcount * (selfcount - 1)
            for count in distanceDict.values():
                total += count * (count - 1)
        return total

class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        length = len(timeSeries)
        if length < 2:
            return length * duration
        i, j = 0, 1
        total = 0
        while j < length:
            total += min(timeSeries[j]-timeSeries[i], duration)
            i += 1
            j += 1
        return total + duration

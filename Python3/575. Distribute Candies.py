class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # return int(len(candies)/2 if len(set(candies)) > len(candies)/2 else len(set(candies)))
        return int(min(len(candies)/2, len(set(candies))))

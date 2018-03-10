class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ordered = sorted(nums, reverse=True) # 76ms
        ranksDict = dict(zip(ordered, range(1, len(nums)+1)))
        ranks = []
        for num in nums:
            if ranksDict[num] == 1:
                ranks.append("Gold Medal")
            elif ranksDict[num] == 2:
                ranks.append("Silver Medal")
            elif ranksDict[num] == 3:
                ranks.append("Bronze Medal")
            else:
                ranks.append(str(ranksDict[num]))
        return ranks

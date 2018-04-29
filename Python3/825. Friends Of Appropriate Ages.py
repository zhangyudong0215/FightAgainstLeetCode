class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        numsDict = collections.defaultdict(int)
        for age in ages:
            numsDict[age] += 1
        ans = 0
        for i in range(1, 121):
            for j in range(1, 121):
                if j <= 0.5*i+7 or j>i or j>100 and i<100:
                    pass
                else:
                    if i != j:
                        ans += numsDict[i] * numsDict[j]
                    else:
                        ans += numsDict[i]*(numsDict[i]-1)
        return ans

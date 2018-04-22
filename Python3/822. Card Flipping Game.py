class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        pairs = list(zip(fronts, backs))
        bads = []
        distincts = []
        for pair in pairs:
            if pair[0] == pair[1]:
                bads.append(pair[0])
            else:
                distincts.append(pair)
        nums = []
        for item in distincts:
            if item[0] not in bads:
                nums.append(item[0])
            if item[1] not in bads:
                nums.append(item[1])
        if not nums:
            return 0
        else:
            return min(nums)

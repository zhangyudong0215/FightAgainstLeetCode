class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = collections.Counter(nums)
        # prev = None
        # avoid = using = 0
        # for k in sorted(count):
        #     if k - 1 != prev:
        #         avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
        #     else:
        #         avoid, using = max(avoid, using), k * count[k] + avoid
        #     prev = k
        # return max(avoid, using)
        
        count = collections.Counter(nums)
        prev = None
        ignore = take = 0
        for k in sorted(count):
            if k-1 != prev:
                ignore, take = max(ignore, take), k*count[k] + max(ignore, take)
            else:
                ignore, take = max(ignore, take), k*count[k] + ignore
            prev = k
        return max(ignore, take)

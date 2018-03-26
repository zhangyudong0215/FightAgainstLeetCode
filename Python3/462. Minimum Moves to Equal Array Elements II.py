class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # moves = [] # 暴力破解, 但是超时了
        # for target in range(min(nums), max(nums)+1):
        #     total = 0
        #     for num in nums:
        #         total += abs(target-num)
        #     moves.append(total)
        # return min(moves)
        
        # nums = sorted(nums) # 没错就是中位数 48ms
        # length = len(nums)
        # if length%2 == 0:
        #     median = [nums[length//2], nums[length//2-1]]
        # else:
        #     median = [nums[length//2]]
        # ans = []
        # for target in median:
        #     total = 0
        #     for num in nums:
        #         total += abs(num-target)
        #     ans.append(total)
        # return min(ans)
        
        median = sorted(nums)[len(nums)//2] # 当len(nums)是偶数时, 离中位数最近的两个数均可
        return sum((abs(num-median) for num in nums))

class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        cache = {}
        def recursion(num, positions): # 76ms
            if num == 1: # 无论最后剩下的position是几, 由于num是1, 都是正确排列
                return 1
            condition = (num, positions) # 需要排列的是num, 剩下的位置是由元组positions储存
            if condition in cache:
                return cache[condition] # 查询此状态是否有记录
            total = 0
            for index in range(len(positions)): # 遍历剩余位置
                if positions[index]%num == 0 or num%positions[index] == 0: # 当前位置positions[index]和num排列合法
                    total += recursion(num-1, positions[: index]+positions[index+1: ]) # 排列num-1, 且positions中去掉positions[index]
            cache[condition] = total
            return total
        return recursion(N, tuple(range(1, N+1)))

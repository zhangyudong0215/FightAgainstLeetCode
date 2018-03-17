class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # ans = [] # 132ms
        # for i in range(num+1):
        #     ans.append(bin(i).count('1')) # 时间复杂度O(n*sizeof(Integer))
        # return ans
        
        # ans = [] # 720ms 位运算
        # for i in range(num+1):
        #     ans.append(sum([(i>>j)&1 for j in range(32)]))
        # return ans
        
        # ans = [] # 288ms 修改的位运算方法, 通过num的大小判断二进制字符最大长度, 减少计算
        # if num == 0:
        #     length = 1
        # else:
        #     length = math.ceil(math.log2(num)) + 1
        # for i in range(num+1):
        #     ans.append(sum([(i>>j)&1 for j in range(length)]))
        # return ans
        
        # ans = [0] # 124ms
        # for i in range(1, num+1):
        #     ans.append(ans[i//2] + i%2)
        # return ans
        
        ans = [0] # 104ms 最快 此方法在golang中几乎等同于上面一种
        while len(ans) <= num + 1:
            ans.extend([i+1 for i in ans])
        return ans[: num+1]

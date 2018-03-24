class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # length = len(temperatures) # 超时了
        # ans = []
        # for i in range(length):
        #     j = i + 1
        #     while j < length and temperatures[j] <= temperatures[i]:
        #         j += 1
        #     if j < length:
        #         ans.append(j-i)
        #     else:
        #         ans.append(0)         
        # return ans
        
        # length = len(temperatures) # 596ms
        # nearest = [length] * 72
        # ans = [0] * length
        # for i in range(length-1, -1, -1):
        #     index = min(nearest[temperatures[i]+1-30: ])
        #     if index < length and index > 0:
        #         ans[i] = index - i
        #     nearest[temperatures[i]-30] = i 
        # return ans
        
        length = len(temperatures) # 300-500ms
        ans = [0 for i in temperatures]
        stack = []
        for i in range(length):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans

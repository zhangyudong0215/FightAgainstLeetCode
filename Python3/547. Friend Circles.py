class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # ans = 0 # 最初版本 104ms, 中间有很多冗余
        # length = len(M)
        # visited = [False] * length
        # def recursion(i):
        #     friends = []
        #     visited[i] = True
        #     for j in list(range(i)) + list(range(i+1, length)):
        #         if M[i][j] == 1 and not visited[j]:
        #             friends.append(j)
        #             visited[j] = True
        #     for j in friends:
        #         friends.extend(recursion(j))
        #     return friends    
        # for i in range(length):
        #     if not visited[i]:
        #         recursion(i)
        #         ans += 1
        # return ans
        
        # ans = 0 # 最初版本 104ms, 中间有很多冗余
        # length = len(M)
        # visited = [False] * length
        # def recursion(i):
        #     friends = []
        #     visited[i] = True
        #     for j in range(length): # 由于visited存在, 所以不需要原始版本的操作, 104ms -> 68ms
        #         if M[i][j] == 1 and not visited[j]:
        #             friends.append(j)
        #             visited[j] = True
        #     for j in friends:
        #         recursion(j) 
        # for i in range(length):
        #     if not visited[i]:
        #         recursion(i)
        #         ans += 1
        # return ans 
        
        # 参考答案
        ans = 0 # 60ms 广度搜索
        visited = set()
        def DFS(node):
            visited.add(node)
            for subnode, value in enumerate(M[node]):
                if value and subnode not in visited:
                    DFS(subnode)
        for node in range(len(M)):
            if node not in visited:
                ans += 1
                DFS(node)
        return ans

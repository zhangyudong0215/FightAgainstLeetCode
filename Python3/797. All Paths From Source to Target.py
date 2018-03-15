class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # target = len(graph) - 1 # 广度搜索 172ms
        # currlevel = [(0, [0])]
        # ans = []
        # while currlevel:
        #     nextlevel = []
        #     while currlevel:
        #         curr, nodes = currlevel.pop()
        #         if curr == target:
        #             ans.append(nodes)
        #         for newnode in graph[curr]:
        #             nextlevel.append((newnode, nodes+[newnode]))
        #     currlevel = nextlevel
        # return ans
            
        # target = len(graph) - 1 # 深度搜索 160ms
        # stack = [(0, [0])]
        # ans = []
        # while stack:
        #     curr, nodes = stack.pop()
        #     if curr == target:
        #         ans.append(nodes)
        #     for newnode in graph[curr]:
        #         stack.append((newnode, nodes+[newnode]))
        # return ans
        
        # ans, target = [], len(graph) - 1 # 递归 168ms
        # def recursion(curr, nodes):
        #     if curr == target:
        #         ans.append(nodes)
        #         return
        #     for newnode in graph[curr]:
        #         recursion(newnode, nodes+[newnode])
        # recursion(0, [0])
        # return ans
                
        ans, target = [], len(graph) - 1 # 参考discuss中的方法, 和上面的写法一样, 但是只需要148ms
        def recursion(i, path):
            if i == LAST:
                ans.append(path)
                return
            for j in graph[i]:
                recursion(j, path + (j,))
        recursion(0, (0, ))
        return ans

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def average(M, i, j):
            row = [-1, 0, 1]
            col = [-1, 0, 1]
            if i == 0:
                row = [0, 1]
            if i == len(M) - 1:
                row = [-1, 0]
            if j == 0:
                col = [0, 1]
            if j == len(M[0]) - 1:
                col = [-1, 0]
            total = 0
            for r in row:
                for c in col:
                    total += M[i+r][j+c]
            return total // (len(row) * len(col))
                    
        N = copy.deepcopy(M)
        r = len(M)
        c = len(M[0])
        for i in range(r):
            for j in range(c):
                N[i][j] = average(M, i, j)
        return N

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        i = j = 0
        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        r = -1
        c = 1
        ans = []
        while True:
            ans.append(matrix[i][j])
            if i == row and j == col:
                break
            i += r
            j += c
            if r == -1 and c == 1:
                if j > col:
                    i += 2
                    j -= 1
                elif i < 0:
                    i += 1
                r, c = c, r
                continue
            if r == 1 and c == -1:
                if i > row:
                    i -= 1
                    j += 2
                elif j < 0:
                    j += 1
                r, c = c, r
                continue
        return ans

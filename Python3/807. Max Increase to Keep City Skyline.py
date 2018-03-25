class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        left = [0] * row
        top = [0] * col
        for i in range(row):
            for j in range(col):
                if grid[i][j] > top[j]:
                    top[j] = grid[i][j]
                if grid[i][j] > left[i]:
                    left[i] = grid[i][j]
        count = 0
        for i in range(row):
            for j in range(col):
                count += min(left[i], top[j]) - grid[i][j]
        return count

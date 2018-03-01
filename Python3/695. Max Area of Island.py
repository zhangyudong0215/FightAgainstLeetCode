class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def countContinusArea(i, j):
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + countContinusArea(i-1, j) + countContinusArea(i+1, j) + countContinusArea(i, j-1) + countContinusArea(i, j+1)
            else:
                return 0

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = countContinusArea(i, j)
                maxArea = max(maxArea, count)
        
        return maxArea

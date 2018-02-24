class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum([self.addBorder(grid, i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]])
    
    def addBorder(self, grid, i, j):
        return ((i == 0 or grid[i-1][j] == 0) + 
                (i == len(grid)-1 or grid[i+1][j] == 0) + 
                (j == 0 or grid[i][j-1] == 0) + 
                (j == len(grid[0])-1 or grid[i][j+1] == 0))

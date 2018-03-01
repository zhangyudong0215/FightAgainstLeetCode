func maxAreaOfIsland(grid [][]int) int {
    max := 0
    count := 0
    for i := range grid {
        for j := range grid[0] {
            count = countArea(&grid, i, j)
            if max < count {
                max = count
            }
        }
    }
    return max
}

func countArea(grid *[][]int, i, j int) int {
    if i >= 0 && i < len(*grid) && j >= 0 && j < len((*grid)[0]) && (*grid)[i][j] == 1 {
        (*grid)[i][j] = 0
        return 1 + countArea(grid, i-1, j) + countArea(grid, i+1, j) + countArea(grid, i, j-1) + countArea(grid, i, j+1)
    } else {
        return 0
    }
}

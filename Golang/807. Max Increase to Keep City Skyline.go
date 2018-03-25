func maxIncreaseKeepingSkyline(grid [][]int) int {
    row := len(grid)
    col := len(grid[0])
    left := make([]int, row)
    top := make([]int, col)
    for i := 0; i < row; i++ {
        for j := 0; j < col; j++ {
            if grid[i][j] > top[j] {
                top[j] = grid[i][j]
            }
            if grid[i][j] > left[i] {
                left[i] = grid[i][j]
            }
        }
    }
    count := 0
    for i := 0; i < row; i++ {
        for j := 0; j < col; j++ {
            count += min(left[i], top[j]) - grid[i][j]
        }
    }
    return count
}

func min(a, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}

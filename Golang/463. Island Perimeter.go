func islandPerimeter(grid [][]int) int {
    ans := 0
    for i, slice := range grid {
        for j, island := range slice {
            if island == 1 {
                ans += addBorder(grid, i, j)
            }
        }
    }
    return ans
}

func addBorder(grid [][]int, i, j int) int {
    count := 0
    xy := map[int][]int{i-1: {j}, i: {j-1, j+1}, i+1: {j}}
    for key, values := range xy {
        for _, value := range values {
            if key < 0 || key == len(grid) || value < 0 || value == len(grid[0]) || grid[key][value] == 0 {
                count++
            }
        }
    }
    return count
}

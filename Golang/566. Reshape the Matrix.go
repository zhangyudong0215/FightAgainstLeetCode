func matrixReshape(nums [][]int, r int, c int) [][]int {
    n := len(nums) // origin row number
    m := len(nums[0]) // origin col number
    if n*m != r*c || n == r {
        return nums
    }
    
    count := 0
    matrix := make([][]int, r)
    
    for i := 0; i < r; i++ {
        matrix[i] = make([]int, c)
        for j := 0; j < c; j++ {
            matrix[i][j] = nums[count/m][count%m]
            count++
        }
    }
    
    return matrix
}
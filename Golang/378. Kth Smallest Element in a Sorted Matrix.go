func kthSmallest(matrix [][]int, k int) int {
    r, c := len(matrix), len(matrix[0])
    left, right := matrix[0][0], matrix[r-1][c-1]
    for left < right {
        mid := (left + right) / 2
        count := 0
        j := c - 1
        for i := 0; i < r; i++ {
            for j >= 0 && matrix[i][j] > mid {
                j--
            }
            count += j + 1
        }
        if count < k {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}

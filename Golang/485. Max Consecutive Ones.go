func findMaxConsecutiveOnes(nums []int) int {
    max_length := 0
    length := 0
    
    for _, num := range nums {
        if num == 1 {
            length++
        } else {
            max_length = max(max_length, length)
            length = 0
        }
    }
    
    return max(max_length, length)
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
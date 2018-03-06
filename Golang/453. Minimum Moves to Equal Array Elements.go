func minMoves(nums []int) int { // 48ms
    length := len(nums)
    min := nums[0]
    count := 0
    for _, num := range nums {
        count += num
        if min > num {
            min = num
        }
    }
    return count - min*length
}

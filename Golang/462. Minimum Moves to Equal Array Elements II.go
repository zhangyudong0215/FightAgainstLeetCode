// func minMoves2(nums []int) int { // 44ms
//     sort.Ints(nums)
//     median := nums[len(nums)/2]
//     ans := 0
//     for _, num := range nums {
//         ans += abs(num, median)
//     }
//     return ans
// }

// func abs(a, b int) int {
//     if a > b {
//         return a - b
//     } else {
//         return b - a
//     }
// }

func minMoves2(nums []int) int { // 16ms
    sort.Ints(nums)
    ans := 0
    i := 0
    j := len(nums) - 1
    for i < j {
        ans += nums[j] - nums[i]
        i++
        j--
    }
    return ans
}

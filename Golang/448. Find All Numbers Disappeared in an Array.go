// func findDisappearedNumbers(nums []int) []int { // 868ms???
//     for _, num := range nums {
//         index := int(math.Abs(float64(num)) - 1)
//         nums[index] = int(-math.Abs(float64(nums[index])))
//     }
//     ans := make([]int, 0, len(nums))
//     for i, num := range nums {
//         if num > 0 {
//             ans = append(ans, i+1)
//         }
//     }
//     return ans
// }

func findDisappearedNumbers(nums []int) []int { // 852ms ???换个时间执行一下
    for i := range nums {
        for nums[i] != nums[nums[i]-1] {
            nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        }
    }
    
    ans := make([]int, 0, len(nums))
    for i, num := range nums {
        if num != i+1 {
            ans = append(ans, i+1)
        }
    }
    return ans
}

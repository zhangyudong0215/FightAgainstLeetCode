// func moveZeroes(nums []int)  { // 150ms-170ms 为什么那么慢？
//     position := 0
//     for index, num := range nums {
//         if num != 0 {
//             nums[position], nums[index] = nums[index], nums[position]
//             position++
//         }
//     }
// }

func moveZeroes(nums []int)  { // 148ms
    total := len(nums)
    position := 0
    
    for _, num := range nums {
        if num != 0 {
            nums[position] = num
            position++
        }
    }
    for position < total {
        nums[position] = 0
        position++
    }
}

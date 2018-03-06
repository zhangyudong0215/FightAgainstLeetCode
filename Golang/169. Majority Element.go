// func majorityElement(nums []int) int { // 32ms
//     threshold := len(nums) / 2
//     numsDict := make(map[int]int, threshold+1)
//     for _, num := range nums {
//         numsDict[num]++
//     }
//     ans := 0
//     for num := range  numsDict {
//         if numsDict[num] > threshold {
//             ans = num
//             break
//         }
//     }
//     return ans
// }

func majorityElement(nums []int) int { // 尝试一下新的写法 // 32ms
    threshold := len(nums) / 2
    numsDict := make(map[int]int, threshold+1)
    for _, num := range nums {
        if numsDict[num]++; numsDict[num] > threshold {
            return num
        }
    }
    return 9999
}

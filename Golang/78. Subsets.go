// func subsets(nums []int) [][]int {
//     if len(nums) == 0 {
//         return [][]int{}
//     }
    
//     length := len(nums)
//     ans := make([][]int, 0, 100) // 可以自定义幂函数
//     ans = append(ans, []int{})
//     ans = append(ans, []int{nums[0]})
//     for i := 1; i < length; i++ {
//         temp := make([][]int, 0, len(ans))
//         for j := 0; j < len(ans); j++ {
//             temp = append(temp, append(ans[j], nums[i]))
//         }
//         ans = append(ans, temp...)
//     }
//     return ans
// }
'''
Golang实现的时候切片居然会出现顺序异常
'''
import (
    "sort"
)

func subsets(nums []int) [][]int {
    res := [][]int{}

    recur(nums, []int{}, &res)

    return res
}

func recur(nums, temp []int, res *[][]int) {
    l := len(nums)
    if l == 0 {
        sort.Ints(temp)
        *res = append(*res, temp)
        return
    }

    recur(nums[:l-1], temp, res)

    recur(nums[:l-1], append([]int{nums[l-1]}, temp...), res)
}

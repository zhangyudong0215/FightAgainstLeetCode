// import "strconv"
// import "strings"

// func countBits(num int) []int { // 2104ms ???
//     ans := make([]int, 0, num+1)
//     for i := 0; i <= num; i++ {
//         s := strconv.FormatInt(int64(i), 2)
//         ans = append(ans, strings.Count(s, "1"))
//     }
//     return ans
// }

// func countBits(num int) []int { // 2164ms ???
//     ans := make([]int, 0, num+1)
//     for i := 0; i <= num; i++ {
//         count := 0
//         j := i
//         for j > 0 {
//             if j&1 == 1 {
//                 count++
//             }
//             j >>= 1
//         }
//         ans = append(ans, count)
//     }
//     return ans
// }

func countBits(num int) []int { // 2108ms
    ans := make([]int, 1, num+1)
    for i := 1; i <= num; i++ {
        ans = append(ans, i%2 + ans[i/2])
    }
    return ans
}

// func singleNumber(nums []int) int {
//     hashtable := make(map[int]int, len(nums)/2+1)
//     for _, num := range nums {
//         if hashtable[num] == 0 {
//             hashtable[num] = 1
//         } else {
//             delete(hashtable, num)
//         }
//     }
//     ans := 0
//     for k, _ := range hashtable {
//         ans = k
//     }
//     return ans
// }

func singleNumber(nums []int) int {
    ans := 0
    
    for _, num := range nums {
        ans ^= num // a^b^c^b^c = a
    }
    
    return ans
}
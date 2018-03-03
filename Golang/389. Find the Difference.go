// func findTheDifference(s string, t string) byte { // 4ms
//     ss := []byte(s)
//     tt := []byte(t)
//     charDict := make(map[byte]int, len(tt))
//     for _, char := range tt {
//         charDict[char]++
//     }
//     for _, char := range ss {
//         charDict[char]--
//     }
//     var ans byte
//     for char, value := range charDict {
//         if value == 1 {
//             ans = char
//         }
//     }
//     return ans
// }

func findTheDifference(s string, t string) byte { // 0ms
    hashtable := make([]int, 26)
    for i := range s {
        hashtable[s[i] - 'a']--
        hashtable[t[i] - 'a']++
    }
    hashtable[t[len(t)-1] - 'a']++
    
    var i int
    for i = 0; i < 26; i++ {
        if hashtable[i] == 1 {
            break
        }
    }
    
    return byte('a' + i)
}

// func firstUniqChar(s string) int { // 44ms
//     countChars := make(map[int]int, 26)
//     for _, char := range s {
//         countChars[int(char) - 'a']++
//     }
//     for i, char := range s {
//         if countChars[int(char) - 'a'] == 1 {
//             return i
//         }
//     }
//     return -1
// }

// func firstUniqChar(s string) int { // 24ms 既然用了ascii码就该用数组
//     countChars := [26]int{}
//     for _, char := range s {
//         countChars[int(char) - 'a']++
//     }
//     for i, char := range s {
//         if countChars[int(char) - 'a'] == 1 {
//             return i
//         }
//     }
//     return -1
// }

func firstUniqChar(s string) int { // 12ms 超快，但是占用更多空间，虽然依然是O(1)的space
    countChars := [256]int{}
    for _, char := range s {
        countChars[int(char)]++
    }
    for i, char := range s {
        if countChars[int(char)] == 1 {
            return i
        }
    }
    return -1
}

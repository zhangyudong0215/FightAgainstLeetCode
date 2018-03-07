// func isAnagram(s string, t string) bool {
//     charDict := make(map[int]int, len(s))
//     for _, char := range s {
//         charDict[int(char) - 'a']++
//     }
//     for _, char := range t {
//         charDict[int(char) - 'a']--
//     }
//     for key := range charDict {
//         if charDict[key] != 0 {
//             return false
//         }
//     }
//     return true
// }

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    } else if len(s) == 0 {
        return true
    } else {
        charDict := [26]int{}
        for i := range s {
            charDict[int(s[i]) - 'a']++
            charDict[int(t[i]) - 'a']--
        }
        for _, count := range charDict {
            if count != 0 {
                return false
            }
        }
        return true
    }
}

// func isSubsequence(s string, t string) bool { // 16ms
//     lens := len(s)
//     lent := len(t)
//     i, j := 0, 0
//     for i < lens && j < lent {
//         if s[i] == t[j] {
//             i++
//         }
//         j++
//     }
//     return i == lens
// }

func isSubsequence(s string, t string) bool { // 16ms
    for _, i := range s {
        index := strings.Index(t, string(i))
        if index == -1 {
            return false
        } else {
            t = t[index+1: ]
        }
    }
    return true
}
// func findWords(words []string) []string { // 采用逐个字符判断方法
//     new_words := make([]string, 0)
//     for _, word := range words {
//         word_lower := strings.ToLower(word)
//         if isOneLineWord(word_lower) {
//             new_words = append(new_words, word)
//         }
//     }
//     return new_words
// }

// func isOneLineWord(word string) bool {
//     set1 := "qwertyuiop"
//     set2 := "asdfghjkl"
//     set3 := "zxcvbnm"
//     if isin(word, set1) || isin(word, set2) || isin(word, set3) {
//         return true
//     } else {
//         return false
//     }
// }

// func isin(word, set string) bool {
//     for _, char := range word {
//         if !strings.Contains(set, string(char)) {
//             return false
//         }
//     }
//     return true
// }

import (
    "regexp"
    "strings"
)

func findWords(words []string) []string {
    ans := make([]string, 0)
    rx := regexp.MustCompile("(^[qwertyuiop]*$|^[asdfghjkl]*$|^[zxcvbnm]*$)")
    for _, word := range words {
        word_lower := strings.ToLower(word)
        w := rx.FindString(word_lower)
        if w != "" {
            ans = append(ans, word)
        }
    }
    return ans
}
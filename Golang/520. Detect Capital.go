// func detectCapitalUse(word string) bool {
//     word1 := strings.ToLower(word)
//     word2 := strings.ToUpper(word)
    
//     s1 := word[:1]
//     s2 := word[1:]
//     var buffer bytes.Buffer
//     buffer.WriteString(strings.ToUpper(s1))
//     buffer.WriteString(strings.ToLower(s2))
//     word3 := buffer.String()
    
//     return word == word1 || word == word2 || word == word3
// }

func detectCapitalUse(word string) bool {
    top := word[:1]
    rear := word[1:]
    if isIn(top, 'A', 'Z') {
        return isIn(rear, 'a', 'z') || isIn(rear, 'A', 'Z')
    } else {
        return isIn(rear, 'a', 'z')
    }
    
}

func isIn(s string, first, last byte) bool {
    for _, char := range []byte(s) {
        if char < first || char > last {
            return false
        }
    }
    return true
}

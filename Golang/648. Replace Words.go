func replaceWords(dict []string, sentence string) string {
    patternDict := make(map[int][]string)
    min_len := len(dict[0])
    max_len := 0
    
    for _, pattern := range dict {
        patternDict[len(pattern)] = append(patternDict[len(pattern)], pattern)
        if len(pattern) < min_len {
            min_len = len(pattern)
        }
        if len(pattern) > max_len {
            max_len = len(pattern)
        }
    }
    
    words := strings.Split(sentence, " ")
    
    for i, word := range words {
        for j := min_len; j <= max_len; j++ {
            for _, pattern := range patternDict[j] {
                if strings.HasPrefix(word, pattern) {
                    words[i] = pattern
                    j = max_len + 1
                    break
                }
            }
        }
    }
    
    return strings.Join(words, " ")
}

func uniqueMorseRepresentations(words []string) int {
    MORSE := [26]string{".-","-...","-.-.","-..",".","..-.","--.",
        "....","..",".---","-.-",".-..","--","-.","---",
        ".--.","--.-",".-.","...","-","..-","...-",".--",
        "-..-","-.--","--.."}
    transforDict := make(map[string]int)
    for _, word := range words {
        transfor := ""
        for _, char := range word {
            transfor += MORSE[int(char)-'a']
        }
        transforDict[transfor]++
    }
    return len(transforDict)
}

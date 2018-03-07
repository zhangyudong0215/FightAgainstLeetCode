func canConstruct(ransomNote string, magazine string) bool {
    charDict := [26]int{}
    for i := range magazine {
        charDict[int(magazine[i]) - 'a']++
    }
    for i := range ransomNote {
        charDict[int(ransomNote[i]) - 'a']--
    }
    for i := range charDict {
        if charDict[i] < 0 {
            return false
        }
    }
    return true
}
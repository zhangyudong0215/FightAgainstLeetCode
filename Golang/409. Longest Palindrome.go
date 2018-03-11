func longestPalindrome(s string) int {
    charDict := [82]int{}
    for _, char := range s {
        charDict[int(char - 'A')]++
    }
    
    ans := 0
    
    for i := range charDict {
        ans += (charDict[i] / 2) * 2
    }
    
    if ans < len(s) {
        return ans + 1
    }
    return ans
}

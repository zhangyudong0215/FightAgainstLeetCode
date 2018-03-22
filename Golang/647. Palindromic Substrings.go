func countSubstrings(s string) int {
    length := len(s)
    ans := 0
    for center := 0; center < 2*length-1; center++ {
        left := center / 2
        right := left + center%2
        for left >= 0 && right < length && s[left] == s[right] {
            ans++
            left--
            right++
        }
    }
    return ans
}

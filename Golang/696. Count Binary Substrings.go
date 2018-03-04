func countBinarySubstrings(s string) int { // 16ms
    ss := []byte(s)
    head := ss[0]
    var ans, prev, cur int
    for _, char := range ss {
        if char != head {
            ans += min(prev, cur)
            head = char
            prev, cur = cur, 1
        } else {
            cur++
        }
    }
    ans += min(prev, cur)
    return ans
}

func min(a, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}

func findContentChildren(g []int, s []int) int {
    sort.Ints(g)
    sort.Ints(s)
    count, index := 0, 0
    len1, len2 := len(g), len(s)
    for count < len1 && index < len2 {
        if g[count] <= s[index] {
            count++
        }
        index++
    }
    return count
}

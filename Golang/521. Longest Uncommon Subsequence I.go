func findLUSlength(a string, b string) int {
    if strings.EqualFold(a, b) {
        return -1
    } else if len(a) > len(b) {
        return len(a)
    } else {
        return len(b)
    }
}

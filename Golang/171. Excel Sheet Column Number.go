func titleToNumber(s string) int {
    length := len(s)
    sum := 0
    factor := 1
    for i := length-1; i >= 0; i-- {
        sum += (int(s[i] - 'A') + 1) * factor
        factor *= 26
    }
    return sum
}

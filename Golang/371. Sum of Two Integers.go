func getSum(a int, b int) int {
    if a == 0 {
        return b
    } else {
        return getSum(a&b<<1, a^b)
    }
}

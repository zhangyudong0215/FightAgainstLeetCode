func hammingDistance(x int, y int) int {
    var a, b, total int
    for {
        if x == 0 && y == 0 {
            break
        }
        a = x % 2
        b = y % 2
        if a != b {
            total++
        }
        x /= 2
        y /= 2
    }
    return total
}
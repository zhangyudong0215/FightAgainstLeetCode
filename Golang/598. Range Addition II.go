func maxCount(m int, n int, ops [][]int) int {
    if len(ops) == 0 {
        return m * n
    } else {
        for _, op := range ops {
            m = min(m, op[0])
            n = min(n, op[1])
        }
        return m * n
    }
}

func min(a, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}

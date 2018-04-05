func integerBreak(n int) int {
    ans := make([]int, n+1)
    ans[1] = 1
    for i := 2; i <= n; i++ {
        ans[i] = ans[i-1]
        for j := 1; j <= 9; j++ {
            if i-j > 0 && ans[i-j]*j > ans[i] {
                ans[i] = ans[i-j] * j
            }
            if i < n && ans[i] < i {
                ans[i] = i
            }
        }
    }
    return ans[n]
}

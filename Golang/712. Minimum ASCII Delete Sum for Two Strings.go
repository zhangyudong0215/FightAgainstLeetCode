func minimumDeleteSum(s1 string, s2 string) int {
    length1 := len(s1)
    length2 := len(s2)
    dp := make([][]int, length1+1)
    
    dp[length1] = make([]int, length2+1)

    for i := length1-1; i >= 0; i-- {
        dp[i] = make([]int, length2+1)
        dp[i][length2] = dp[i+1][length2] + int(s1[i])
    }
    for j := length2-1; j >= 0; j-- {
        dp[length1][j] = dp[length1][j+1] + int(s2[j])
    }

    for i := length1-1; i >= 0; i-- {
        for j := length2-1; j >= 0; j-- {
            if s1[i] == s2[j] {
                dp[i][j] = dp[i+1][j+1]
            } else {
                dp[i][j] = int(math.Min(float64(dp[i+1][j]+int(s1[i])), float64(dp[i][j+1]+int(s2[j]))))
            }
        }
    }
    return dp[0][0]
}
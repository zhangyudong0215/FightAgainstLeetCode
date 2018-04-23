func minDistance(word1 string, word2 string) int {
    dp := make([][]int, len(word2)+1)
    for i := 0; i <= len(word2); i++ {
        dp[i] = make([]int, len(word1)+1)
    }
    for i := 0; i <= len(word2); i++ {
        dp[i][0] = i
    }
    for i := 0; i <= len(word1); i++ {
        dp[0][i] = i
    }
    
    for i := 1; i <= len(word2); i++ {
        for j := 1; j <= len(word1); j++ {
            if word2[i-1] == word1[j-1] {
                dp[i][j] = dp[i-1][j-1]
            } else {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            }
        }
    }
    
    return dp[len(word2)][len(word1)]
}

func min(a, b int) int {
    if a > b {
        return b
    } else {
        return a
    }
}

func maxProfit(prices []int) int {
    ans := 0
    length := len(prices)
    if length < 2 {
        return 0
    } else {
        for i := 0; i < length-1; i++ {
            if prices[i] < prices[i+1] {
                ans += prices[i+1] - prices[i]
            }
        }
        return ans
    }
}

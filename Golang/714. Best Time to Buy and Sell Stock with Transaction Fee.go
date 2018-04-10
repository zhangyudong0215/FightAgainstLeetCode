func maxProfit(prices []int, fee int) int {
    cash, hold := 0, -prices[0]
    for i := 1; i < len(prices); i++ {
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    }
    return cash
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}

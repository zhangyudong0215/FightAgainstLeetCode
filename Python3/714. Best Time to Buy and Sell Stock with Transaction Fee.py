class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # # 方法1
        # state = profit = 0 
        # last_price = prices[0] 
        # for price in prices[1:]:                  
        #     state += price - last_price
        #     if state > fee:
        #         profit += state - fee
        #         state = fee
        #     elif state < 0: 
        #         state = 0
        #     last_price = price
        # return profit
        
        # # 方法2
        # buy = prices[0]
        # res = 0
        # for p in prices:
        #     if buy > p: # current price is less than last buy
        #         buy = p # buy at p
        #     else:
        #         tmp = p - buy - fee
        #         if tmp > 0: # have profit
        #             res += tmp
        #             buy = p - fee 
        # return res
        
        # # 方法3 DP
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

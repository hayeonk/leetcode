class Solution(object):
    def maxProfit(self, prices, fee):
        cash = 0
        hold = -prices[0]
        for i in xrange(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
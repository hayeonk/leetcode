class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        ans = 0
        for i in xrange(len(prices)-1):
            if prices[i] < prices[i+1]:
                ans += prices[i+1] - prices[i]
        return ans
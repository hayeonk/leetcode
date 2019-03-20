class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        ret = 0
        minVal = prices[0]
        for i in xrange(1, len(prices)):
            ret = max(ret, prices[i] - minVal)
            minVal = min(minVal, prices[i])
        
        return ret
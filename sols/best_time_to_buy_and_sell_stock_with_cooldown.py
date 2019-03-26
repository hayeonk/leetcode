class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        
        n = len(prices)
        s0 = [0] * n
        s1 = [0] * n
        s2 = [0] * n
        s1[0] = -prices[0]
        s2[0] = -987654321
        
        for i in xrange(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
        return max(s0[-1], s2[-1])
        
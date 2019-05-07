class Solution(object):
    def minCostII(self, costs):
        if not costs:
            return 0
        
        dp = costs[0]
        k = len(costs[0])
        for row in costs[1:]:
            nextdp = row
            for i in xrange(k):
                nextdp[i] += min(dp[:i] + dp[i+1:])
            dp = nextdp
        return min(dp)
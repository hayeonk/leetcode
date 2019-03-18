class Solution(object):
    def minCostClimbingStairs(self, cost):
        ret = [cost[0], cost[1]]
        for i in xrange(2, len(cost)):
            ret[i%2] = cost[i] + min(ret)
        return min(ret)
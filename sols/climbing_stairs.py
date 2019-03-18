class Solution(object):
    def climbStairs(self, n):
        ret = [1, 2]
        for i in xrange(2, n):
            ret.append(ret[i-1] + ret[i-2])
        return ret[n-1]
            
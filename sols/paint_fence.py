class Solution(object):
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        
        same = k
        diff = k * (k - 1)
        for i in xrange(2, n):
            same, diff = diff, (same + diff) * (k-1)
            
        return same + diff
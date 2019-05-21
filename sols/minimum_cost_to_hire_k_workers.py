from heapq import *
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted([(float(w) / q, q, w) for q, w in zip(quality, wage)])
        
        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heappush(pool, -q)
            sumq += q
            
            if len(pool) > K:
                sumq += heappop(pool)
            
            if len(pool) == K:
                ans = min(ans, ratio * sumq)
        
        return ans
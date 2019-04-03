import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        cand = [1]
        
        for i in xrange(n):
            ans = heapq.heappop(cand)
            for p in 2, 3, 5:
                if ans * p not in cand:
                    heapq.heappush(cand, ans * p)
            
        return ans
        
from heapq import *
class Solution(object):
    def lastStoneWeight(self, stones):
        heap = []
        for n in stones:
            heappush(heap, -n)
        
        while len(heap) >= 2:
            n1 = -heappop(heap)
            n2 = -heappop(heap)
            
            if n1 == n2:
                continue
            
            heappush(heap, -abs(n1 - n2))
        
        if not heap:
            return 0
        return -heappop(heap)
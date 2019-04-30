from collections import defaultdict
from heapq import *

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        
        if src not in adj:
            return -1
        
        q = [(0, src, 0)]
        while q:
            p, s, cnt = heappop(q)
            if s == dst:
                return p
            if cnt < K + 1:
                for d, price in adj[s]:
                    heappush(q, (p + price, d, cnt+1))
                    
        return -1
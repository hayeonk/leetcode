import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v-1, w))
        
        dist = {}
        pq = [(0, K-1)]
        while pq:
            d, u = heapq.heappop(pq)
            if u in dist: continue
            dist[u] = d
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(pq, (d + w, v))
        return max(dist.values()) if len(dist) == N else -1
            
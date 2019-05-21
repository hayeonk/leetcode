from heapq import *
class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0
        
        n = len(heightMap)
        m = len(heightMap[0])
        visit = [[0] * m for _ in xrange(n)]
        pq = []
        
        for j in xrange(m):
            heappush(pq, (heightMap[0][j], 0, j))
            heappush(pq, (heightMap[n-1][j], n-1, j))
            visit[0][j] = visit[n-1][j] = 1
        
        for i in xrange(n):
            heappush(pq, (heightMap[i][0], i, 0))
            heappush(pq, (heightMap[i][m-1], i, m-1))
            visit[i][0] = visit[i][m-1] = 1
        
        ans = 0
        maxHeight = 0
        while pq:
            height, i, j = heappop(pq)
            ans += max(0, maxHeight - height)
            maxHeight = max(maxHeight, height)
            
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < n and 0 <= nj < m and not visit[ni][nj]:
                    visit[ni][nj] = 1
                    heappush(pq, (heightMap[ni][nj], ni, nj))
        return ans
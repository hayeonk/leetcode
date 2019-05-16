from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        n = len(grid)
        m = len(grid[0])
        dist = [[0] * m for _ in xrange(n)]
        count = [[0] * m for _ in xrange(n)]
        
        def bfs(i, j):
            visit = [[0] * m for _ in xrange(n)]
            visit[i][j] = 1
            q = deque([[0, i, j]])
            
            while q:
                d, i, j = q.popleft()
                dist[i][j] += d
                count[i][j] += 1
                
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0 and not visit[ni][nj]:
                        q.append((d+1, ni, nj))
                        visit[ni][nj] = 1
        
        buildingCnt = 0
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    bfs(i, j)
                    buildingCnt += 1
                    
        ans = float('inf')
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 0 and count[i][j] == buildingCnt:
                    ans = min(ans, dist[i][j])

        return ans if ans != float('inf') else -1
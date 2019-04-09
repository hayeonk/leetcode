from collections import deque

class Solution(object):
    def islandPerimeter(self, grid):
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        
        visit = {}
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    q.append([i, j])
                    visit[(i, j)] = 1
                    break
        
        ans = 0
        adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            i, j = q.popleft()
            
            for x, y in adj:
                if 0 <= i+x < n and 0 <= j+y < m and grid[i+x][j+y] == 1:
                    if (i+x, j+y) not in visit:
                        visit[(i+x, j+y)] = 1
                        q.append([i+x, j+y])
                else:
                    ans += 1
        return ans
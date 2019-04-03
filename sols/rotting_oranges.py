from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        count = 0
        q = deque([])
        
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
                elif grid[i][j] == 1:
                    count += 1
        
        visit = {}
        ans = 0
        while q and count:
            i, j, d = q.popleft()
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visit:
                continue
            
            visit[(i, j)] = 1
            if grid[i][j] == 1:
                count -= 1
                grid[i][j] = 2
                ans = max(ans, d)
            
            if grid[i][j] == 2:
                q += [[i+1, j, d+1], [i-1, j, d+1], [i, j+1, d+1], [i, j-1, d+1]]
        
        return -1 if count else ans
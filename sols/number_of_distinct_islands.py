class Solution(object):
    def numDistinctIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        visit = set()
        island = set()
        
        def dfs(i, j):
            points = set()
            s = [(i, j)]
            
            while s:
                y, x = s.pop()
                visit.add((y, x))
                points.add((y-i, x-j))
                
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in visit and grid[ny][nx] == 1:
                        s.append((ny, nx))
            island.add(tuple(points))
                        
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1 and (i, j) not in visit:
                    dfs(i, j)
            
        return len(island)
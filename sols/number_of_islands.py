class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visit or grid[i][j] != '1':
                return

            visit[(i, j)] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        n = len(grid)
        m = len(grid[0])
        visit = {}
        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == "1" and (i, j) not in visit:
                    ans += 1
                    bfs(i, j)
        return ans
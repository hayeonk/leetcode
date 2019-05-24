class Solution(object):
    def uniquePathsIII(self, grid):
        n = len(grid)
        m = len(grid[0])
        count = 0
        
        for i in xrange(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 2:
                    end = [i, j]
                elif grid[i][j] == 0:
                    count += 1
        
        self.ans = 0
        def makePath(path, visited):
            if len(path) == count + 2 and path[-1] == end:
                self.ans += 1
                return
            
            i, j = path[-1]
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                    if grid[ni][nj] == 0 or grid[ni][nj] == 2:
                        visited.add((ni, nj))
                        makePath(path + [[ni, nj]], visited)
                        visited.remove((ni, nj))
        
        makePath([start], set())
        return self.ans
from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        if not matrix:
            return matrix
        
        n = len(matrix)
        m = len(matrix[0])
        
        q = deque([])
        visit = [[0] * m for _ in xrange(n)]
        
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 0:
                    q.append([i, j, 0])
        
        while q:
            i, j, dist = q.popleft()
            if i < 0 or i >= n or j < 0 or j >= m or visit[i][j]:
                continue
                
            visit[i][j] = 1
            matrix[i][j] = dist
            q += [[i+1, j, dist+1], [i-1, j, dist+1], [i, j+1, dist+1], [i, j-1, dist+1]]
            
        return matrix
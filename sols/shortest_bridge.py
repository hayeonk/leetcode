from collections import deque

class Solution(object):
    def shortestBridge(self, A):
        n = len(A)
        m = len(A[0])
        q = deque([])
        visit = {}
        
        def dfs(i, j, n, m):
            if i < 0 or i >= n or j < 0 or j >= m or A[i][j] != 1 or (i, j) in visit:
                return
            
            q.append([i, j, 0])
            visit[(i, j)] = 1
            
            dfs(i+1, j, n, m)
            dfs(i-1, j, n, m)
            dfs(i, j+1, n, m)
            dfs(i, j-1, n, m)
            
        for i in xrange(n):
            check = False
            for j in xrange(m):
                if A[i][j] == 1:
                    dfs(i, j, n, m)
                    check = True
                    break
            if check:
                break
        
        newVisit = {}
        while q:
            i, j, d = q.popleft()
            if i < 0 or i >= n or j < 0 or j >= m or (i, j) in newVisit:
                continue
                
            if (i, j) not in visit and A[i][j] == 1:
                return d-1
            
            newVisit[(i, j)] = 1
            q += [(i+1, j, d+1), (i-1, j, d+1), (i, j+1, d+1), (i, j-1, d+1)]
        
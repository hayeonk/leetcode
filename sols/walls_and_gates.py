from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        INF = 2 ** 31 - 1
        if not rooms or not rooms[0]:
            return
        
        n = len(rooms)
        m = len(rooms[0])
        
        q = deque([])
        visited = set()
        for i in xrange(n):
            for j in xrange(m):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while q:
            i, j, d = q.popleft()
            rooms[i][j] = min(rooms[i][j], d)
            
            for k in xrange(4):
                x = i + dy[k]
                y = j + dx[k]
                
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited and rooms[x][y] != -1:
                    q.append((x, y, d + 1))
                    visited.add((x, y))
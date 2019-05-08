class Solution(object):
    def hasPath(self, maze, start, destination):
        n = len(maze)
        m = len(maze[0])
        
        def getNextPos(i, j, di, dj):
            while 0 <= i + di < n and 0 <= j + dj < m and maze[i+di][j+dj] == 0:
                i += di
                j += dj
            return i, j
        
        visit = set()
        stack = [start]
        
        while stack:
            i, j = stack.pop()
            if [i, j] == destination:
                return True
            
            visit.add((i, j))
            
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = getNextPos(i, j, di, dj)
                if (ni, nj) not in visit:
                    stack.append((ni, nj))
        return False
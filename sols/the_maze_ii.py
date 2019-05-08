from heapq import *
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        n = len(maze)
        m = len(maze[0])
        
        def getNextPos(i, j, di, dj):
            while 0 <= i + di < n and 0 <= j + dj < m and maze[i+di][j+dj] == 0:
                i += di
                j += dj
            return i, j
        
        visit = {}
        pq = [(0, start[0], start[1])]
        
        while pq:
            d, i, j = heappop(pq)
            if (i, j) in visit and visit[(i, j)] <= d:
                continue
            
            if [i, j] == destination:
                return d
            
            visit[(i, j)] = d
            
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = getNextPos(i, j, di, dj)
                heappush(pq, (abs(ni-i) + abs(nj-j) + d, ni, nj))
        
        return -1
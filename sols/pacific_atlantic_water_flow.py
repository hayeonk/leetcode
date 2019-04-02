from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.m = defaultdict(set)
        
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        def startFrom(i, j, si, sj, pi, pj, visit):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visit:
                return
            if matrix[i][j] > matrix[pi][pj]:
                return
            
            if (i, j) in self.m:
                self.m[(si, sj)] |= self.m[(i, j)]
                return
            
            if i == 0 or j == 0:
                self.m[(si, sj)].add(1)
            if i == m-1 or j == n-1:
                self.m[(si, sj)].add(2)
            
            visit[(i, j)] = 1
            
            startFrom(i+1, j, si, sj, i, j, visit)
            startFrom(i-1, j, si, sj, i, j, visit)
            startFrom(i, j+1, si, sj, i, j, visit)
            startFrom(i, j-1, si, sj, i, j, visit)
        
        for i in xrange(m):
            for j in xrange(n):
                startFrom(i, j, i, j, i, j, {})
        
        ret = []
        for i, j in self.m:
            if len(self.m[(i, j)]) == 2:
                ret += [[i, j]]
        return ret
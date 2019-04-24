class Solution(object):
    def findCircleNum(self, M):
        n = len(M)
        group = range(n)
        
        def find(u):
            if u == group[u]:
                return u
            group[u] = find(group[u])
            return group[u]
        
        def union(u, v):
            u = find(u)
            v = find(v)
            if u == v:
                return
            group[u] = v
        
        for i in xrange(n):
            for j in xrange(i+1, n):
                if M[i][j]:
                    union(i, j)
        
        return len(set([find(x) for x in group]))
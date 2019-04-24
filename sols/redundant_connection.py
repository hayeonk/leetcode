class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        group = range(n+1)
        
        def find(u):
            if group[u] != u:
                group[u] = find(group[u])
            return group[u]
        
        def union(u, v):
            u = find(u)
            v = find(v)
            if u == v:
                return True
            group[u] = v
            return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
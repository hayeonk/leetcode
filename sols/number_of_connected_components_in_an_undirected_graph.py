class Solution(object):
    def countComponents(self, n, edges):
        group = range(n)
        
        def find(u):
            if group[u] != u:
                group[u] = find(group[u])
            return group[u]
        
        def union(u, v):
            u = find(u)
            v = find(v)
            
            if u != v:
                group[u] = v
        
        for u, v in edges:
            union(u, v)
        
        return len(set([find(i) for i in xrange(n)]))
class Solution(object):
    def removeStones(self, stones):
        n = len(stones)
        group = range(n)
        
        def find(u):
            if group[u] != u:
                group[u] = find(group[u])
            return group[u]
        
        def union(u, v):
            u = find(u)
            v = find(v)
            if u == v:
                return
            group[u] = v
            
        for i in xrange(n):
            for j in xrange(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        
        ans = n - len(set([find(u) for u in group]))
        return ans
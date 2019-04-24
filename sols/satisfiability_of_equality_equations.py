class Solution(object):
    def equationsPossible(self, equations):
        def chrToInt(c):
            return ord(c) - ord("a")
        
        def find(u):
            if group[u] != u:
                group[u] = find(group[u])
            return group[u]
        
        def union(u, v):
            u = find(u)
            v = find(v)
            if u == v:
                return u
            group[u] = v
            return v
        
        group = range(26)
        
        for eq in equations:
            u = chrToInt(eq[0])
            v = chrToInt(eq[3])
            if eq[1] == "=":
                union(u, v)
        
        for eq in equations:
            u = chrToInt(eq[0])
            v = chrToInt(eq[3])
            if eq[1] == "!":
                if find(u) == find(v):
                    return False
        return True
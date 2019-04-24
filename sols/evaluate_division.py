from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        d = defaultdict(list)
        for i in xrange(len(equations)):
            a, b = equations[i]
            if a not in d:
                d[a].append((a, 1.0))
            if b not in d:
                d[b].append((b, 1.0))
            d[a].append((b, values[i]))
            d[b].append((a, 1.0 / values[i]))
        
        def find(u, end):
            if u not in d:
                return -1.0
            
            visit = defaultdict(int)
            visit[u] = 1
            q = [(u, 1.0)]
            while q:
                u, n1 = q.pop()
                if u == end:
                    return n1
                for v, n2 in d[u]:
                    if not visit[v]:
                        visit[v] = 1
                        q.append((v, n1 * n2))
            return -1.0
        
        ans = []
        for a, b in queries:
            ans.append(find(a, b))
        return ans
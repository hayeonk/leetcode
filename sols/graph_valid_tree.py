from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(u):
            visit.add(u)
            
            if u in graph:
                for v in graph[u]:
                    if v not in visit:
                        dfs(v)
            
        visit = set()
        dfs(0)
        
        return len(visit) == n
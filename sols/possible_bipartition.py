from collections import defaultdict
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        color = {}
        def dfs(node, c):
            if node in color:
                return color[node] == c
            
            color[node] = c
            for nei in graph[node]:
                if not dfs(nei, c ^ 1):
                    return False
            return True
        
        for u in xrange(N):
            if u not in color:
                if not dfs(u, 0):
                    return False
        
        return True
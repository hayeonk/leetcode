class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        groups = {}
        
        def dfs(i):
            for j in graph[i]:
                if j in groups: 
                    if groups[j] == groups[i]:
                        return False
                else:
                    groups[j] = 1 - groups[i]
                    if not dfs(j):
                        return False
            return True
        
        for i in xrange(n):
            if i not in groups:
                groups[i] = 0
            if not dfs(i):
                return False
        return True
from collections import defaultdict
class Solution(object):
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)
        
        def dfs(u):
            if color[u] != WHITE:
                return color[u] == BLACK
            
            color[u] = GRAY
            for v in graph[u]:
                if color[v] == BLACK:
                    continue
                if color[v] == GRAY or not dfs(v):
                    return False
            color[u] = BLACK
            return True
        
        ans = []
        n = len(graph)
        for u in xrange(n):
            if dfs(u):
                ans.append(u)
        return ans
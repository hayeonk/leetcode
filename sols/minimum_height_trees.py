from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        graph = [[] for _ in xrange(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        if n == 1:
            return [0]
        
        leaves = [i for i in xrange(n) if len(graph[i]) == 1]
        
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves
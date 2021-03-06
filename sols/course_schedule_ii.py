class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        n = numCourses
        graph = [[] for _ in xrange(n)]
        for a, b in prerequisites:
            graph[b].append(a)
        
        order = []
        visited = [False] * n
        inprocess = [False] * n
        
        def dfs(a):
            visited[a] = inprocess[a] = True
            
            for b in graph[a]:
                if not visited[b]:
                    if dfs(b):
                        return True
                elif inprocess[b]:
                    return True
            
            order.append(a)
            inprocess[a] = False
            return False
        
        for i in xrange(n):
            if not visited[i]:
                if dfs(i):
                    return []
        order.reverse()
        return order
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        n = numCourses
        graph = [[] for _ in xrange(n)]
        for a, b in prerequisites:
            graph[b].append(a)
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
            inprocess[a] = False
            return False
            
        ans = False
        for i in xrange(n):
            if not visited[i]:
                ans |= dfs(i)
        return not ans
        
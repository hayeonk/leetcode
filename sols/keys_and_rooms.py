class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visit = [0] * n
        
        def dfs(u):
            visit[u] = 1
            for v in rooms[u]:
                if not visit[v]:
                    dfs(v)
        
        dfs(0)
        return all(visit)
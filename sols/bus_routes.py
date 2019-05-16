from collections import defaultdict, deque
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        
        n = len(routes)
        d = defaultdict(list)
        q = deque()
        end = set()
        
        for i in xrange(n):
            if S in routes[i]:
                q.append([i, 1])
            
            if T in routes[i]:
                end.add(i)
                
            for j in xrange(i+1, n):
                if set(routes[i]) & set(routes[j]):
                    d[i].append(j)
                    d[j].append(i)
        
        visit = set()
        while q:
            u, dist = q.popleft()
            if u in end:
                return dist
            
            visit.add(u)
            for v in d[u]:
                if v not in visit:
                    q.append([v, dist + 1])
        return -1
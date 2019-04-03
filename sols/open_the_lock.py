from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        visit = {}
        q = deque([[(0, 0, 0, 0), 0]])
        target = tuple(map(int, target))
        deadends = [tuple(map(int, x)) for x in deadends]
        
        while q:
            s, dist = q.popleft()
            if s in visit or s in deadends:
                continue

            visit[s] = dist
            
            if s == target:
                return dist
            
            for i in xrange(4):
                q.append([s[:i] + tuple([(s[i]+1)%10]) + s[i+1:], dist + 1])
                q.append([s[:i] + tuple([(s[i]-1)%10]) + s[i+1:], dist + 1])
            
        return -1
        
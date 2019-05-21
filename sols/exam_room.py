from bisect import *
class ExamRoom(object):
    def __init__(self, N):
        self.seated = []
        self.last = N - 1
        
    def seat(self):
        if not self.seated:
            self.seated.append(0)
            return 0
        
        ret = 0
        maxDist = 0
        n = len(self.seated)
        for i in xrange(n):
            if i == 0 and 0 not in self.seated:
                pos = 0
                dist = self.seated[0]
                if dist > maxDist:
                    maxDist = dist
                    ret = pos
            else:
                pos = (self.seated[i-1] + self.seated[i]) / 2
                dist = min(pos - self.seated[i-1], self.seated[i] - pos)
                if dist > maxDist:
                    maxDist = dist
                    ret = pos
                
            if i == n - 1:
                pos = self.last
                dist = pos - self.seated[-1]
                if dist > maxDist:
                    maxDist = dist
                    ret = pos
                
        insort(self.seated, ret)
        return ret
        
    def leave(self, p):
        self.seated.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
from collections import deque
class HitCounter(object):
    def __init__(self):
        self.q = deque([])
        
    def hit(self, timestamp):
        self.q.append(timestamp)

    def getHits(self, timestamp):
        while self.q and self.q[0] <= timestamp - 300:
            self.q.popleft()
        return len(self.q)
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
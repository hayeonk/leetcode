from collections import deque
class MovingAverage(object):
    def __init__(self, size):
        self.size = size
        self.q = deque()
        self.curSum = 0.0

    def next(self, val):
        self.curSum += float(val)
        self.q.append(val)
        if len(self.q) > self.size:
            self.curSum -= self.q.popleft()
        return self.curSum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
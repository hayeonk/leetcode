import random
from bisect import *
class Solution(object):
    def __init__(self, w):
        self.psum = []
        self.total = 0
        for n in w:
            self.total += n
            self.psum.append(self.total)

    def pickIndex(self):
        target = random.randint(0, self.total - 1)
        idx = bisect(self.psum, target)
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
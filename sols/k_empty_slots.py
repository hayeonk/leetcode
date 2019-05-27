from bisect import *
class Solution(object):
    def kEmptySlots(self, bulbs, K):
        bulb = []
        for i, b in enumerate(bulbs):
            idx = bisect_left(bulb, b)
            if idx > 0 and b - bulb[idx-1] == K + 1:
                return i + 1
            if idx < len(bulb) and bulb[idx] - b == K + 1:
                return i + 1
            insort(bulb, b)
        return -1
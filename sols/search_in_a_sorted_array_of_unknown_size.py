import sys
class Solution(object):
    def search(self, reader, target):
        lo, hi = 0, 1
        INF = 2147483647
        while reader.get(hi) != INF:
            hi *= 2
        
        while lo <= hi:
            mid = (lo + hi) / 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target or reader.get(mid) == INF:
                hi = mid - 1
            else:
                lo = mid + 1
                
        return -1
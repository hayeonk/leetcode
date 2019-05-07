from collections import defaultdict
class Solution(object):
    def isReflected(self, points):
        d = defaultdict(list)
        for x, y in points:
            d[y].append(float(x))
        
        mid = None
        for y in d:
            l = sorted(set(d[y]))
            i, j = 0, len(l)-1
            while i <= j:
                m = (l[i] + l[j]) / 2
                if mid is None:
                    mid = m
                elif mid != m:
                    return False
                i += 1
                j -= 1
        return True
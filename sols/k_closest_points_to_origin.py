from heapq import *
class Solution(object):
    def kClosest(self, points, K):
        distance = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heappush(distance, (dist, [x, y]))
        
        return [x[1] for x in nsmallest(K, distance)]
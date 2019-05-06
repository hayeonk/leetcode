from heapq import *

class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort()
        pq = []
        ans = 0
        
        for s, e in intervals:
            if not pq or pq[0] > s:
                heappush(pq, e)
                ans = max(ans, len(pq))
            else:
                heappop(pq)
                heappush(pq, e)
                
        return ans
class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        cnt = 0
        end = -float('inf')
        
        for interval in points:
            if interval[0] > end:
                cnt += 1
                end = interval[1]
        return cnt
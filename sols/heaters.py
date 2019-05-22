from bisect import *
class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        ans = 0
        
        for house in houses:
            idx = bisect(heaters, house)
            dist = abs(heaters[idx] - house)
            if idx > 0:
                dist = min(dist, abs(heaters[idx-1] - house))
            if idx < len(heaters) - 1:
                dist = min(dist, abs(heaters[idx+1] - house))
            
            ans = max(ans, dist)
        
        return ans
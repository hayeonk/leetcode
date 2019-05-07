class Solution(object):
    def maxDistance(self, arrays):
        n = len(arrays)
        ans = 0
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        
        for i in xrange(1, n):
            ans = max(ans, abs(arrays[i][-1] - minVal))
            ans = max(ans, abs(maxVal - arrays[i][0]))
            
            minVal = min(minVal, arrays[i][0])
            maxVal = max(maxVal, arrays[i][-1])
        
        return ans
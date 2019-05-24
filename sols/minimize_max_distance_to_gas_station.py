class Solution(object):
    def minmaxGasDist(self, stations, K):
        def possible(dist, K):
            count = 0
            for i in xrange(len(stations) - 1):
                d = stations[i+1] - stations[i]
                count += int(d / dist)
                if count > K:
                    return False
            
            return True
        
        stations = map(float, stations)
        maxDist = 0.0
        for i in xrange(len(stations) - 1):
            maxDist = max(maxDist, stations[i+1] - stations[i])
        
        lo, hi = 0.0, maxDist
        ans = maxDist
        for _ in xrange(50):
            mid = (lo + hi) / 2.0
            if possible(mid, K):
                ans = min(ans, mid)
                hi = mid
            else:
                lo = mid
        return ans
            
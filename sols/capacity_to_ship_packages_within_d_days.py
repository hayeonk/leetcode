class Solution(object):
    def shipWithinDays(self, weights, D):
        def canSend(maxCap):
            cnt = 1
            curWei = 0
            for w in weights:
                if curWei + w > maxCap:
                    curWei = w
                    cnt += 1
                else:
                    curWei += w
            return cnt <= D
        
        lo, hi = max(weights), sum(weights)
        ans = hi
        while lo <= hi:
            mid = (lo + hi) / 2
            if canSend(mid):
                ans = min(ans, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
class Solution(object):
    def minEatingSpeed(self, piles, H):
        def canEat(K, H):
            cnt = 0
            for n in piles:
                cnt += n / K
                if n % K:
                    cnt += 1
            return cnt <= H
        
        lo, hi = 1, max(piles)
        ans = hi
        
        while lo <= hi:
            mid = (lo + hi) / 2
            if canEat(mid, H):
                ans = min(ans, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
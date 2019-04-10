from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        d = defaultdict(int)
        lo = hi = 0
        ans = 0
        
        while hi < len(s):
            d[s[hi]] += 1
            hi += 1
            while sum(sorted(d.values())[:-1]) > k:
                d[s[lo]] -= 1
                if d[s[lo]] == 0:
                    del d[s[lo]]
                lo += 1
            ans = max(ans, hi - lo)
        
        return ans
from collections import defaultdict
from bisect import *
class Solution(object):
    def minWindow(self, S, T):
        if not S or not T:
            return ""
        
        d = defaultdict(list)
        
        for i, c in enumerate(S):
            d[c].append(i)
        
        ans = None
        while d[T[0]]:
            startIdx = d[T[0]].pop(0)
            idx = startIdx
            check = True
            for c in T[1:]:
                i = bisect(d[c], idx)
                if i >= len(d[c]):
                    check = False
                    break
                idx = d[c][i]
                
            if not check:
                break
            else:
                if ans is None or len(ans) > idx - startIdx + 1:
                    ans = S[startIdx:idx+1]
        
        return "" if ans is None else ans
from heapq import *
from collections import Counter

class Solution(object):
    def reorganizeString(self, S):
        n = len(S)
        S = Counter(S)
        if max(S.values()) > (n + 1) / 2:
            return ""
        
        ans = []
        pq = [(-S[c], c) for c in S]
        heapify(pq)
        
        while len(pq) >= 2:
            cnt1, ch1 = heappop(pq)
            cnt2, ch2 = heappop(pq)
            ans.extend([ch1, ch2])
            if cnt1 + 1:
                heappush(pq, (cnt1+1, ch1))
            if cnt2 + 1:
                heappush(pq, (cnt2+1, ch2))
        
        return "".join(ans) + (pq[0][1] if pq else "")
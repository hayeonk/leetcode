from collections import Counter
class Solution(object):
    def subarraysDivByK(self, A, K):
        C = Counter()
        C[0] += 1
        
        cur = 0 
        for n in A:
            cur = (cur + n) % K
            C[cur] += 1
        
        ans = 0
        for c in C:
            ans += C[c] * (C[c]-1) / 2
        return ans
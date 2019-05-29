from collections import Counter
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        AB = Counter([a + b for a in A for b in B])
        CD = Counter([c + d for c in C for d in D])
        ans = 0
        
        for n in AB:
            ans += AB[n] * CD[-n]
        
        return ans
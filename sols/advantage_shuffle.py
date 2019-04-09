from collections import defaultdict

class Solution(object):
    def advantageCount(self, A, B):
        A.sort()
        lo, hi = 0, len(A)-1
        d = defaultdict(list)
        
        for n in sorted(B, reverse=True):
            if n < A[hi]:
                d[n].append(A[hi])
                hi -= 1
            else:
                d[n].append(A[lo])
                lo += 1
        
        return [d[n].pop() for n in B]
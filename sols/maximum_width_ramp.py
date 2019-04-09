from bisect import bisect
class Solution(object):
    def maxWidthRamp(self, A):
        if not A:
            return 0
        
        maxVal = 0
        l = [[A[0], 0]]
        for i in xrange(1, len(A)):
            if l[-1][1] > A[i]:
                l.append([i, A[i]])
            else:
                for val, idx in reversed(l):
                    if val <= A[i]:
                        maxVal = max(maxVal, i - idx)
                    else:
                        break
        return maxVal
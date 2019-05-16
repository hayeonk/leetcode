class Solution(object):
    def partitionDisjoint(self, A):
        leftmax, rightmin = [], []
        n = len(A)
        
        for i in xrange(n):
            if not leftmax:
                leftmax.append(A[i])
            else:
                leftmax.append(max(leftmax[-1], A[i]))
        
        for i in xrange(n-1, -1, -1):
            if not rightmin:
                rightmin.append(A[i])
            else:
                rightmin.append(min(rightmin[-1], A[i]))
        
        rightmin = rightmin[::-1]
        
        for i in xrange(n-1):
            if leftmax[i] <= rightmin[i+1]:
                return i + 1
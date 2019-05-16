class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        ans = 0
        for i in xrange(len(A) - 2):
            if A[i] + A[i+1] > A[i+2]:
                ans = A[i] + A[i+1] + A[i+2]
        return ans
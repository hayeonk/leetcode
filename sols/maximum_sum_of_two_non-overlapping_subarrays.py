class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        for i in xrange(1, len(A)):
            A[i] += A[i-1]
        
        ans, Lmax, Mmax = A[L+M-1], A[L-1], A[M-1]
        for i in xrange(L+M, len(A)):
            Lmax = max(Lmax, A[i-M] - A[i-M-L])
            Mmax = max(Mmax, A[i-L] - A[i-M-L])
            ans = max(ans, Lmax + A[i] - A[i-M], Mmax + A[i] - A[i-L])
        return ans
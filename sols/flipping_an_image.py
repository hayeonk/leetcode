class Solution(object):
    def flipAndInvertImage(self, A):
        for i in xrange(len(A)):
            A[i].reverse()
        
        for i in xrange(len(A)):
            for j in xrange(len(A[i])):
                A[i][j] = 0 if A[i][j] else 1
        return A
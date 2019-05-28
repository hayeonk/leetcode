class Solution(object):
    def sortArrayByParityII(self, A):
        even = []
        odd = []
        
        for i in xrange(len(A)):
            if i % 2 == 0 and A[i] % 2 != 0:
                even.append(i)
            if i % 2 == 1 and A[i] % 2 != 1:
                odd.append(i)
    
        for i, j in zip(even, odd):
            A[i], A[j] = A[j], A[i]
        return A
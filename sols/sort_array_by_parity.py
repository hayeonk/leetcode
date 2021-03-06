class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            while i < j and A[i] % 2 == 0:
                i += 1
            while i < j and A[j] % 2 == 1:
                j -= 1
            
            if i == j:
                break
                
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A
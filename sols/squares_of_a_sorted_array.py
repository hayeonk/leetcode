class Solution(object):
    def sortedSquares(self, A):
        i, j = 0, len(A) - 1
        ans = []
        
        while i <= j:
            n1 = A[i] * A[i]
            n2 = A[j] * A[j]
            if n1 > n2:
                ans.append(n1)
                i += 1
            else:
                ans.append(n2)
                j -= 1
            
        return ans[::-1]
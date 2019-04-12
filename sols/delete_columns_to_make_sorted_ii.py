class Solution(object):
    def minDeletionSize(self, A):
        n = len(A)
        ans = i = 0
        
        while sorted(A) != A:
            col = [s[:i+1] for s in A]
            if sorted(col) == col:
                i += 1
            else:
                A = [s[:i] + s[i+1:] for s in A]
                ans += 1
        
        return ans
class Solution(object):
    def longestOnes(self, A, K):
        i = zeroCnt = 0
        ans = 0
        for j in xrange(len(A)):
            if A[j] == 0:
                zeroCnt += 1
            while zeroCnt > K:
                if A[i] == 0:
                    zeroCnt -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans
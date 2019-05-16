class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0
        for j in xrange(len(S)):
            if S[i] != S[j]:
                if j - i >= 3:
                    ans.append([i, j-1])
                i = j
        if len(S) - i >= 3:
            ans.append([i, len(S)-1])
        return ans
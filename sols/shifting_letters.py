class Solution(object):
    def shiftingLetters(self, S, shifts):
        n = len(shifts)
        for i in xrange(n-2, -1, -1):
            shifts[i] += shifts[i+1]
            shifts[i] %= 26
        
        S = list(S)
        for i in xrange(n):
            S[i] = chr(ord('a') + (ord(S[i]) - ord('a') + shifts[i]) % 26)
        return "".join(S)
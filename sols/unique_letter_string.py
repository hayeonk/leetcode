class Solution(object):
    def uniqueLetterString(self, S):
        MOD = 10 ** 9 + 7
        
        n = len(S)
        left = [0] * n
        right = [0] * n
        
        d = {}
        for i in xrange(n):
            c = S[i]
            cnt = i + 1
            if c in d:
                cnt -= d[c] + 1
            left[i] = cnt
            d[c] = i
            
        d = {}
        for i in xrange(n):
            c = S[n-i-1]
            cnt = i + 1
            if c in d:
                cnt -= d[c] + 1
            right[n-i-1] = cnt
            d[c] = i
        
        return sum(l * r for l, r in zip(left, right)) % MOD
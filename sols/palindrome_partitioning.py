class Solution(object):
    def partition(self, s):
        n = len(s)
        isPalindrome = [[0] * n for _ in xrange(n)]
        for i in xrange(n):
            isPalindrome[i][i] = 1
            if i > 0 and s[i-1] == s[i]:
                isPalindrome[i-1][i] = 1
        
        for i in reversed(xrange(n)):
            for j in xrange(i+2, n):
                if s[i] == s[j] and isPalindrome[i+1][j-1]:
                    isPalindrome[i][j] = 1
        
        ret = []
        def backtrack(picked, idx):
            if idx >= len(s):
                ret.append(picked)
                return
            
            for j in xrange(idx, len(s)):
                if isPalindrome[idx][j]:
                    backtrack(picked + [s[idx:j+1]], j + 1)
        
        backtrack([], 0)
        return ret
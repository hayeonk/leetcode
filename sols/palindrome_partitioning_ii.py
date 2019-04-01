class Solution(object):
    def minCut(self, s):
        n = len(s)
        isPalindrome = [[0] * n for _ in xrange(n)]
        d = range(n)
        d.reverse()
        for i in xrange(n):
            isPalindrome[i][i] = 1
            if i > 0 and s[i-1] == s[i]:
                isPalindrome[i-1][i] = 1
        
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if isPalindrome[i][j] or (s[i] == s[j] and isPalindrome[i+1][j-1]):
                    isPalindrome[i][j] = 1
                    if j == n - 1:
                        d[i] = 0
                    else:
                        d[i] = min(d[i], d[j + 1] + 1)
        
        return d[0]
        
class Solution(object):
    def longestPalindrome(self, s):
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
            
        if not s:
            return s
        
        n = len(s)
        start = end = 0
        for i in xrange(n):
            len1 = expand(i, i)
            len2 = expand(i, i+1)
            maxLen = max(len1, len2)
            if maxLen > end - start:
                start = i - (maxLen - 1) / 2
                end = i + maxLen / 2
        return s[start:end+1]
    
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""
        
        C = Counter(t)
        window = Counter()
        
        def containAll(window, C):
            for c in C:
                if window[c] < C[c]:
                    return False
            return True
        
        i = 0
        minLen = float('inf')
        ans = ""
        
        for j in xrange(len(s)):
            window[s[j]] += 1
            while containAll(window, C):
                if j - i + 1 < minLen:
                    minLen = j - i + 1
                    ans = s[i:i+minLen]
                window[s[i]] -= 1
                i += 1
        return ans
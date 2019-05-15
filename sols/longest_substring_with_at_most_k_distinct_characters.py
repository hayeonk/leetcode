class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        d = {}
        
        ans = i = 0
        for j in xrange(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            while len(d) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        
        d = {s[0]: 1}
        ans = 1
        start = 0
        for i in xrange(1, len(s)):
            while s[i] in d:
                del d[s[start]]
                start += 1
            d[s[i]] = 1
            ans = max(ans, i - start + 1)
        return ans
                
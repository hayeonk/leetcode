from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        i = ans = 0
        d = defaultdict(int)
        
        for j in xrange(len(s)):
            d[s[j]] += 1
            
            while len(d) > 2:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                i += 1
            
            ans = max(ans, j - i + 1)
        
        return ans
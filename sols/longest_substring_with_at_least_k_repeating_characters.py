from collections import Counter
import re

class Solution(object):
    def longestSubstring(self, s, k):
        print s
        if len(s) < k:
            return 0
        
        freq = Counter(s)
        notValid = []
        for c in freq:
            if freq[c] < k:
                notValid += [c]
        
        if not notValid:
            return len(s)
        
        ans = 0
        s = re.split("|".join(notValid), s)
        for c in s:
            ans = max(ans, self.longestSubstring(c, k))
        return ans
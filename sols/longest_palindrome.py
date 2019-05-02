from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        C = Counter(s)
        ans = 0
        one = 0
        
        for x in C:
            ans += (C[x] / 2) * 2
            one = max(one, int(C[x] % 2))
        
        return ans + one
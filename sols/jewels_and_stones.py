from collections import Counter

class Solution(object):
    def numJewelsInStones(self, J, S):
        S = Counter(S)
        ans = 0
        for c in J:
            if c in S:
                ans += S[c]
        return ans
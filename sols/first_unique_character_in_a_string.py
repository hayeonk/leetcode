from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        freq = Counter(s)
        for i, c in enumerate(s):
            if freq[c] < 2:
                return i
        return -1
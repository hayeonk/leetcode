from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        s = Counter(s)
        ans = ""
        for n, c in sorted(s.items(), key=lambda x: x[1], reverse=True):
            ans += c * n
        return ans
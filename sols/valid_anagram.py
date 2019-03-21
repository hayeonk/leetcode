from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        s = Counter(s)
        t = Counter(t)
        return s == t
class Solution(object):
    def findTheDifference(self, s, t):
        ret = 0
        for c in s:
            ret ^= ord(c)
        for c in t:
            ret ^= ord(c)
        return chr(ret)
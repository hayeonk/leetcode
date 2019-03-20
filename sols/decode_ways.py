class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        ret = [1] + [0] * n
        if s[0] != "0":
            ret[1] = 1
        
        for i in xrange(2, len(s)+1):
            first = int(s[i-1])
            second = int(s[i-2:i])
            if first >= 1 and first <= 9:
                ret[i] += ret[i-1]
            if second >= 10 and second <= 26:
                ret[i] += ret[i-2]

        return ret[-1]
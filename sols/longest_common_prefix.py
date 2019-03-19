class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        n = min(len(s) for s in strs)
        ret = ""
        for i in xrange(n):
            check = True
            for j in xrange(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    check = False
            if check:
                ret += strs[0][i]
            else:
                break
        return ret
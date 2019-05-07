class Solution(object):
    def generatePossibleNextMoves(self, s):
        if "++" not in s:
            return []
        
        ans = []
        for i in xrange(len(s)-1):
            if s[i:i+2] == "++":
                ans.append(s[:i] + "--" + s[i+2:])
        return ans
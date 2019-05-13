class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        d = {}
        for i, src, dst in zip(indexes, sources, targets):
            if S[i:i+len(src)] == src:
                d[(i, i+len(src))] = dst
        
        ans = ""
        last = 0
        
        for i, j in sorted(d):
            ans += S[last:i]
            ans += d[(i, j)]
            last = j
        ans += S[last:len(S)]
        return ans
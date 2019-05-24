class Solution(object):
    def longestStrChain(self, words):
        words = set(words)
        d = {}
        
        def getMaxLen(word):
            if word in d:
                return d[word]
            
            ret = 0
            for i in xrange(len(word)):
                if word[:i] + word[i+1:] in words:
                    ret = max(ret, 1 + getMaxLen(word[:i] + word[i+1:]))
            
            d[word] = ret
            return ret
        
        ans = 0
        for word in words:
            ans = max(ans, getMaxLen(word))
        return ans + 1
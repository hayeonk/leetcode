class Solution(object):
    def wordPatternMatch(self, pattern, str):
        patternToStr = {}
        strToPattern = {}
        
        def canMatch(i, j):
            if i == len(pattern):
                return j == len(str)
            
            if j == len(str):
                return i == len(pattern)
            
            if pattern[i] in patternToStr:
                word = patternToStr[pattern[i]]
                if str[j:j+len(word)] == word:
                    return canMatch(i + 1, j + len(word))
                else:
                    return False
            
            for k in xrange(j + 1, len(str) + 1):
                if str[j:k] not in strToPattern:
                    patternToStr[pattern[i]] = str[j:k]
                    strToPattern[str[j:k]] = pattern[i]
                    if canMatch(i + 1, k):
                        return True
                    del patternToStr[pattern[i]]
                    del strToPattern[str[j:k]]
            
            return False
        
        return canMatch(0, 0)
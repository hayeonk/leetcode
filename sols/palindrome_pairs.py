class Solution(object):
    def palindromePairs(self, words):
        def isPalindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        d = {}
        for i, word in enumerate(words):
            d[word] = i
            
        ans = []
        
        for word in d:
            n = len(word)
            for j in xrange(n+1):
                pref = word[:j]
                suf = word[j:]
                
                if isPalindrome(pref):
                    pair = suf[::-1]
                    if pair != word and pair in d:
                        ans.append([d[pair], d[word]])
                
                if j != n and isPalindrome(suf):
                    pair = pref[::-1]
                    if pair != word and pair in d:
                        ans.append([d[word], d[pair]])
        return ans
from collections import deque
class Solution(object):
    def expressiveWords(self, S, words):
        def encode(s):
            ret = deque()
            i = 0
            for j in xrange(len(s)):
                if s[j] != s[i]:
                    ret.append((s[i], j - i))
                    i = j
            ret.append((s[i], len(s) - i))
            return ret
        
        def canStretch(s, word):
            while s and word:
                a, n1 = s.popleft()
                b, n2 = word.popleft()
                if a == b and n1 == n2:
                    continue
                if a != b or n2 > n1:
                    return False
                if n1 < 3:
                    return False
            return not s and not word
                    
        ans = 0
        for word in words:
            s = encode(S)
            word = encode(word)
            if canStretch(s, word):
                ans += 1
        return ans
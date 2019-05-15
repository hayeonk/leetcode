class Solution(object):
    def numMatchingSubseq(self, S, words):
        ans = 0
        heads = [[] for _ in xrange(26)]
        for word in words:
            heads[ord(word[0]) - ord('a')].append(word)
        
        for c in S:
            idx = ord(c) - ord('a')
            l = heads[idx]
            heads[idx] = []
            
            while l:
                word = l.pop()[1:]
                if not word:
                    ans += 1
                    continue
                heads[ord(word[0]) - ord('a')].append(word)
        return ans
class Solution(object):
    def boldWords(self, words, S):
        def makeBold(start, end):
            for i in xrange(start, end):
                bold[i] = 1
                
        n = len(S)
        bold = [0] * n
        
        for word in words:
            for i in xrange(n - len(word) + 1):
                if S[i:i+len(word)] == word:
                    makeBold(i, i + len(word))
        
        ans = []
        for i in xrange(n):
            if bold[i] and (i == 0 or not bold[i-1]):
                ans.append("<b>")
            
            if i > 0 and not bold[i] and bold[i-1]:
                ans.append("</b>")
                
            ans.append(S[i])
            if bold[i] and i == n - 1:
                ans.append("</b>")
                
        return "".join(ans)
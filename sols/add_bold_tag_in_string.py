class Solution(object):
    def addBoldTag(self, s, dict):
        bold = [0] * len(s)
        
        def makeBold(start, end):
            for i in xrange(start, end):
                bold[i] = 1
                
        for word in dict:
            idx = 0
            while word in s[idx:]:
                idx += s[idx:].index(word)
                makeBold(idx, idx + len(word))
                idx += 1
        
        if not any(bold):
            return s
        
        if all(bold):
            return "<b>" + s + "</b>"
        
        ans = ""
        
        i = None
        for j in xrange(len(s)):
            if bold[j] == 0:
                if i is not None:
                    ans += s[i:j]
                    ans += "</b>"
                ans += s[j]
                i = None
            else:
                if i is None:
                    ans += "<b>"
                    i = j
        if i:
            ans += s[i:j+1]
            ans += "</b>"
            
        return ans
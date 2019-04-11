class Solution(object):
    def fullJustify(self, words, maxWidth):
        def makeString(cur, maxWidth, last):
            n = len(cur)
            
            if n == 1:
                return cur[0] + " " * space
               
            if last:
                s = " ".join(cur)
                s += " " * (maxWidth - len(s))
                return s
            
            space = maxWidth - sum(len(word) for word in cur)
            spaceEach = space / (n - 1)
            addSpace = space % (n - 1)
            
            for i, word in enumerate(cur):
                if i < addSpace:
                    s += word + " " * (spaceEach + 1)
                elif i == n - 1:
                    s += word
                else:
                    s += word + " " * spaceEach
            
            return s
            
        ans = []
        cur = []
        curLen = 0
        for i, word in enumerate(words):
            if curLen + len(word) > maxWidth:
                ans.append(makeString(cur, maxWidth, False))
                cur = [word]
                curLen = len(word) + 1
            else:
                cur.append(word)
                curLen += len(word) + 1
                
        if cur:
            ans.append(makeString(cur, maxWidth, True))
        
        return ans
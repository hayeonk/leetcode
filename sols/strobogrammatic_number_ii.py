class Solution(object):
    def findStrobogrammatic(self, n):
        valid = ["0", "1", "6", "8", "9"]
        middle = ["0", "1", "8"]
        
        ans = []
        half = []
        
        def makeHalf(cur, n):
            if n == 0:
                half.append(cur)
                return
            
            if not cur:
                for c in valid[1:]:
                    makeHalf(c, n - 1)
            else:
                for c in valid:
                    makeHalf(cur + c, n - 1)
        
        makeHalf("", n / 2)
        
        def makeWhole(s, idx):
            ret = s
            for i in xrange(idx, -1, -1):
                if s[i] == "6":
                    ret += "9"
                elif s[i] == "9":
                    ret += "6"
                else:
                    ret += s[i]
            return ret
            
        if n % 2:
            for s in half:
                for c in middle:
                    ans.append(makeWhole(s + c, len(s)-1))
            
        else:
            for s in half:
                ans.append(makeWhole(s, len(s)-1))
        
        return ans
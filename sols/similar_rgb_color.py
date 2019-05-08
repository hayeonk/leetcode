class Solution(object):
    def similarRGB(self, color):
        def getMostSimilar(s):
            hexDigit = "0123456789abcdef"
            num = int(s, 16)
            ret = None
            dist = float('inf')
            for h in hexDigit:
                d =  (int(h*2, 16) - num) ** 2
                if d < dist:
                    dist = d
                    ret = h * 2
            return ret
        
        ans = "#"
        for i in xrange(1, 7, 2):
            ans += getMostSimilar(color[i:i+2])
        return ans
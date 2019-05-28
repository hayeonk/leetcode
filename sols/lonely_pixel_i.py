from collections import Counter
class Solution(object):
    def findLonelyPixel(self, picture):
        if not picture or not picture[0]:
            return 0
        
        n = len(picture)
        m = len(picture[0])
        
        row = Counter()
        col = Counter()
        
        for i in xrange(n):
            for j in xrange(m):
                if picture[i][j] == "B":
                    row[i] += 1
                    col[j] += 1
        
        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                if picture[i][j] == "B" and row[i] == 1 and col[j] == 1:
                    ans += 1
        return ans
from collections import defaultdict
class Solution(object):
    def findBlackPixel(self, picture, N):
        if not picture or not picture[0]:
            return 0
        
        n = len(picture)
        m = len(picture[0])
        
        row = defaultdict(list)
        col = defaultdict(list)
        
        for i in xrange(n):
            for j in xrange(m):
                if picture[i][j] == "B":
                    row[i].append(j)
                    col[j].append(i)
        
        ans = 0
        for i in xrange(n):
            for j in xrange(m):
                if picture[i][j] == "B" and len(row[i]) == len(col[j]) == N:
                    check = True
                    for k in xrange(1, N):
                        if row[col[j][k]] != row[col[j][k-1]]:
                            check = False
                    if check:
                        ans += 1
        return ans
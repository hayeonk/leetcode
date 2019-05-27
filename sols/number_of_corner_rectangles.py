from collections import defaultdict
class Solution(object):
    def countCornerRectangles(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        d = defaultdict(list)
        
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    d[i].append(j)
        
        ans = 0
        for x in d:
            for y in d:
                if x == y:
                    continue
                
                l1 = d[x]
                l2 = d[y]
                
                i = j = 0
                cnt = 0
                while i < len(l1) and j < len(l2):
                    if l1[i] == l2[j]:
                        cnt += 1
                        i += 1
                        j += 1
                    elif l1[i] < l2[j]:
                        i += 1
                    else:
                        j += 1
                
                ans += cnt * (cnt - 1) / 2
        
        return ans / 2
from collections import defaultdict
class Solution(object):
    def minAreaRect(self, points):
        d = defaultdict(list)
        for x, y in points:
            d[x].append(y)
            
        ans = float('inf')
        l = d.keys()
        for i in xrange(len(l)):
            for j in xrange(i+1, len(l)):
                l1 = sorted(d[l[i]])
                l2 = sorted(d[l[j]])
                p1 = p2 = 0
                last = None
                while p1 < len(l1) and p2 < len(l2):
                    if l1[p1] == l2[p2]:
                        if last is None:
                            last = l1[p1]
                        else:
                            area = abs(l1[p1] - last) * abs(l[i] - l[j])
                            ans = min(ans, area)
                            last = l1[p1]
                        p1 += 1
                        p2 += 1
                    elif l1[p1] < l2[p2]:
                        p1 += 1
                    else:
                        p2 += 1
                            
        return ans if ans != float('inf') else 0
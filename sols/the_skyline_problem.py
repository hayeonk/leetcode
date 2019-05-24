from bisect import *
class Solution(object):
    def getSkyline(self, buildings):
        ans = []
        ends = []
        
        for start, end, height in buildings:
            while ends and ends[0][0] < start:
                x, y = ends.pop(0)
                if not ends:
                    ans.append([x, 0])
                else:
                    ans.append([x, ends[0][1]])
            
            if not ans or ans[-1][1] < height:
                if ans and ans[-1][0] == start:
                    ans[-1][1] = max(ans[-1][1], height)
                else:
                    ans.append([start, height])
            
            idx = bisect(ends, [end, ])
            if idx < len(ends) and ends[idx][0] == end:
                ends[idx][1] = max(ends[idx][1], height)
            elif idx < len(ends) and ends[idx][1] > height:
                continue
            else:
                insort(ends, [end, height])
            
            idx -= 1
            while idx >= 0 and ends[idx][1] <= height:
                ends.pop(idx)
                idx -= 1
        
        while ends:
            x, y = ends.pop(0)
            if not ends:
                ans.append([x, 0])
            else:
                ans.append([x, ends[0][1]])
            
        return ans
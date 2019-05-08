from collections import defaultdict
class Solution(object):
    def anagramMappings(self, A, B):
        d = defaultdict(list)
        for i, n in enumerate(B):
            d[n].append(i)
            
        ans = []
        for n in A:
            ans.append(d[n].pop())
        return ans
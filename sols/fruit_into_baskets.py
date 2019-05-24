from collections import Counter
class Solution(object):
    def totalFruit(self, tree):
        ans = i = 0
        C = Counter()
        
        for j in xrange(len(tree)):
            C[tree[j]] += 1
            while len(C) > 2:
                C[tree[i]] -= 1
                if C[tree[i]] == 0:
                    del C[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
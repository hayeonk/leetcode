class Solution(object):
    def findLongestChain(self, pairs):
        if not pairs:
            return 0
        
        pairs.sort(key=lambda x: x[1])
        ans = [pairs[0]]
        
        for i in xrange(1, len(pairs)):
            if pairs[i][0] > ans[-1][1]:
                ans.append(pairs[i])
        return len(ans)
class Solution(object):
    def candy(self, ratings):
        if not ratings:
            return 0
        
        n = len(ratings)
        ans = [1] * n
        
        for i in xrange(1, n):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
                
        for j in xrange(n-1, 0, -1):
            if ratings[j-1] > ratings[j] and ans[j-1] <= ans[j]:
                ans[j-1] = ans[j] + 1
        
        return sum(ans)
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        n = len(customers)
        ans = sum(customers[:X]) + sum([customers[i] for i in xrange(X, n) if grumpy[i] == 0])
        cur = ans
        
        for i in xrange(X, n):
            cur += customers[i] * grumpy[i]
            cur -= customers[i-X] * grumpy[i-X]
            ans = max(ans, cur)
        return ans
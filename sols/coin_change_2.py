class Solution(object):
    def change(self, amount, coins):
        A = [1] + [0] * amount
        for c in coins:
            for j in xrange(1, amount+1):
                if j >= c:
                    A[j] += A[j-c]
        return A[amount]
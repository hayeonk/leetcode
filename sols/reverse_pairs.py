from bisect import *
class Solution(object):
    def reversePairs(self, nums):
        A = []
        ans = 0
        
        for n in nums[::-1]:
            idx = bisect_right(A, (n-1) / 2)
            ans += idx
            insort(A, n)
        return ans
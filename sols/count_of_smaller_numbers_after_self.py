from bisect import *
class Solution(object):
    def countSmaller(self, nums):
        A = []
        ans = []
        for num in nums[::-1]:
            idx = bisect_left(A, num)
            ans.append(idx)
            insort(A, num)

        return ans[::-1]
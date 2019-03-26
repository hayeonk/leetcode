class Solution(object):
    def findDuplicate(self, nums):
        d = {}
        for n in nums:
            if n in d:
                return n
            d[n] = 1
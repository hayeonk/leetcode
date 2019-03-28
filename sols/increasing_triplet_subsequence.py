import sys
class Solution(object):
    def increasingTriplet(self, nums):
        small = big = sys.maxint
        for n in nums:
            if n <= small:
                small = n
            elif n <= big:
                big = n
            else:
                return True
        return False
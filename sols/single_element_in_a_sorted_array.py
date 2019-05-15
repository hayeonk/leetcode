class Solution(object):
    def singleNonDuplicate(self, nums):
        ans = 0
        for n in nums:
            ans ^= n
        return ans
class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        n = len(nums)
        idx = n / 2
        return sum([abs(x - nums[idx]) for x in nums])
class Solution(object):
    def canJump(self, nums):
        if not nums:
            return False
        
        n = len(nums)
        i, maxJump = 0, 0
        while i <= maxJump and i < n:
            maxJump = max(maxJump, i + nums[i])
            i += 1
        return maxJump >= n-1
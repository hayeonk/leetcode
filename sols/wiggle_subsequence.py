class Solution(object):
    def wiggleMaxLength(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        
        ans = 0
        direction = None
        for i in xrange(1, len(nums)):
            if direction is None:
                if nums[i] > nums[i-1]:
                    direction = 1
                elif nums[i] < nums[i-1]:
                    direction = -1
            else:
                if (nums[i] - nums[i-1]) * direction < 0:
                    ans += 1
                    direction *= -1
        
        return ans + 2 if direction else 1
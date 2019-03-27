class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        left = 0
        for i in xrange(1, n):
            if nums[i-1] <= nums[i]:
                left = i
            else:
                break
                
        if left == n-1:
            return 0
        
        right = n-1
        for i in reversed(xrange(n-1)):
            if nums[i] <= nums[i+1]:
                right = i
            else:
                break
        
        rightMin = min(nums[left+1:])
        leftMax = max(nums[:right])
        while left >= 0 and nums[left] > rightMin:
            left -= 1
        while right <= n-1 and nums[right] < leftMax:
            right += 1
        return right - left - 1
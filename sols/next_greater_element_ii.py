class Solution(object):
    def nextGreaterElements(self, nums):
        if not nums:
            return nums
        
        n = len(nums)
        ans = [-1] * n
        stack = []
        stack.append(max(nums))
        idx = nums.index(max(nums))
        
        for i in xrange(idx-1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        
        for i in xrange(n-1, idx, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums[i])
        
        return ans
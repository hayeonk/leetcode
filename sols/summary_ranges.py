class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        ans = []
        cur = [nums[0]]
        for i in xrange(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                ans.append("->".join(map(str, cur)))
                cur = [nums[i]]
            else:
                cur[1:] = [nums[i]]
        
        ans.append("->".join(map(str, cur)))
        return ans
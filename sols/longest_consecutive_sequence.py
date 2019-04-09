class Solution(object):
    def longestConsecutive(self, nums):
        maxLen = 0
        nums = set(nums)
        
        for num in nums:
            if num - 1 not in nums:
                cur = num
                curLen = 1
                
                while cur + 1 in nums:
                    cur += 1
                    curLen += 1
                    
                maxLen = max(maxLen, curLen)
        
        return maxLen
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        idx = 1
        remove = False
        for i in xrange(1, n):
            if nums[i-1] != nums[i]:
                remove = False
                nums[idx] = nums[i]
                idx += 1
            else:
                if not remove:
                    remove = True
                    nums[idx] = nums[i]
                    idx += 1
                    
        return idx
class Solution(object):
    def findDuplicates(self, nums):
        ret = set()
        for i in xrange(len(nums)):
            while nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    ret.add(nums[i])
                    break
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp
        
        return list(ret)
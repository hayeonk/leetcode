class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        def canPartition(idx, used, k, curSum, targetSum):
            if curSum == targetSum:
                return canPartition(0, used, k-1, 0, targetSum)
            if k == 1:
                return True
            for i in xrange(idx, len(nums)):
                if not used[i] and curSum + nums[i] <= targetSum:
                    used[i] = 1
                    if canPartition(i+1, used, k, curSum + nums[i], targetSum):
                        return True
                    used[i] = 0
            return False
            
        if len(nums) < k or sum(nums) % k != 0:
            return False
        
        n = len(nums)
        targetSum = sum(nums)/k
        used = [0] * n
        return canPartition(0, used, k, 0, targetSum)
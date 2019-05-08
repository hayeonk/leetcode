class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        ans = 0
        n = len(nums)
        
        for i in xrange(n-2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    ans += k - j
                    j += 1
                else:
                    k -= 1
        return ans
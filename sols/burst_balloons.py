class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        m = {}
        
        def burst(left, right):
            if left + 1 == right:
                return 0
            
            if (left, right) in m:
                return m[(left, right)]
            
            ans = 0
            for i in xrange(left + 1, right):
                ans = max(ans, nums[left] * nums[i] * nums[right] + burst(left, i) + burst(i, right))
            
            m[(left, right)] = ans
            return ans
        
        return burst(0, n - 1)
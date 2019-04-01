class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        
        def cmpFunction(a, b):
            if int(a+b) < int(b+a):
                return -1
            elif int(a+b) > int(b+a):
                return 1
            return 0
        
        nums.sort(cmp=cmpFunction, reverse=True)
        ans = "".join(nums)
        if int(ans) == 0:
            return "0"
        return ans
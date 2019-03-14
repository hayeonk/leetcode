class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i, x in enumerate(nums):
            if target - x in dict:
                return [dict[target-x], i]
            dict[x] = i
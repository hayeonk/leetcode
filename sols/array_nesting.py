class Solution(object):
    def arrayNesting(self, nums):
        visit = [0] * len(nums)
        maxVal = 0
        
        for i in xrange(len(nums)):
            if not visit[nums[i]]:
                select = set()
                cur = nums[i]
                while cur not in select:
                    select.add(cur)
                    visit[cur] = 1
                    cur = nums[cur]
                maxVal = max(maxVal, len(select))
        
        return maxVal
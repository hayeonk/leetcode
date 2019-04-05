class Solution(object):
    def rotate(self, nums, k):
        if not nums or k == 0:
            return
        
        n = len(nums)
        start = 0
        cnt = 0
        while cnt < n:
            curIdx, nextIdx = start, (start + k) % n
            tmp = nums[curIdx]
            while nextIdx != start:
                nums[nextIdx], tmp = tmp, nums[nextIdx]
                curIdx = nextIdx
                nextIdx = (curIdx + k) % n
                cnt += 1
            nums[nextIdx] = tmp
            cnt += 1
            start += 1
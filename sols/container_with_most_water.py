class Solution(object):
    def maxArea(self, height):
        lo, hi = 0, len(height)-1
        ret = 0
        while lo <= hi:
            ret = max(ret, (hi - lo) * min(height[lo], height[hi]))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return ret
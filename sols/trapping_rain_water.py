class Solution(object):
    def trap(self, height):
        left = []
        right = []
        
        for h in height:
            if not left:
                left.append(h)
            else:
                left.append(max(left[-1], h))
        
        for h in reversed(height):
            if not right:
                right.append(h)
            else:
                right.insert(0, max(right[0], h))
        
        ans = 0
        for i in xrange(1, len(height)-1):
            ans += min(left[i], right[i]) - height[i]
        return ans
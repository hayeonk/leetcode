class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        d = {}
        stack = []
        for n in reversed(nums2):
            while stack and n > stack[-1]:
                stack.pop()
            
            if not stack:
                d[n] = -1
                
            elif n < stack[-1]:
                d[n] = stack[-1]
            
            stack.append(n)
        
        ans = []
        for n in nums1:
            ans.append(d[n])
        return ans
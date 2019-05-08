class Solution(object):
    def findPermutation(self, s):
        ans = []
        stack = []
        j = 0
        for i in xrange(1, len(s) + 1):
            if s[i-1] == "I":
                stack.append(i)
                while stack:
                    ans.append(stack.pop())
            else:
                stack.append(i)
        
        stack.append(len(s) + 1)
        while stack:
            ans.append(stack.pop())
        return ans
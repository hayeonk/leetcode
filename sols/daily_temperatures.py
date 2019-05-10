class Solution(object):
    def dailyTemperatures(self, T):
        n = len(T)
        ans = [0] * n
        stack = []
        
        for i in xrange(n-1, -1, -1):
            while stack and stack[-1][0] <= T[i]:
                stack.pop()
                
            if stack:
                ans[i] = stack[-1][1] - i
            
            stack.append((T[i], i))
        
        return ans
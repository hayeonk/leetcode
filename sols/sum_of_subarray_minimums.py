class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7
        ans = dot = 0
        stack = []
        
        for val in A:
            cnt = 1
            while stack and stack[-1][0] >= val:
                x, c = stack.pop()
                cnt += c
                dot -= x * c
            
            stack.append((val, cnt))
            dot += val * cnt
            ans += dot
        
        return ans % MOD
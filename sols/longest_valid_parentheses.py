class Solution(object):
    def longestValidParentheses(self, s):
        ans = 0
        stack = [-1]
        for i, c in enumerate(list(s)):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans
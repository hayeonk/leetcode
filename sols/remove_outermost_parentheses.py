class Solution(object):
    def removeOuterParentheses(self, S):
        ans = []
        stack = []
        openCnt = closeCnt = 0
        
        for c in S:
            if c == "(":
                openCnt += 1
            else:
                closeCnt += 1
            
            stack.append(c)
            
            if openCnt == closeCnt:
                ans.append("".join(stack[1:-1]))
                stack = []
        
        return "".join(ans)
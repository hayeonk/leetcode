class Solution(object):
    def removeInvalidParentheses(self, s):
        self.validSet = set()
        self.length = 0
        
        def backtrack(picked, openCnt, closeCnt, s):
            if not s:
                if openCnt == closeCnt:
                    if len(picked) > self.length:
                        self.length = len(picked)
                        self.validSet = set(["".join(picked)])
                    elif len(picked) == self.length:
                        self.validSet.add("".join(picked))
                return
            
            c = s[0]
            if c == "(":
                backtrack(picked, openCnt, closeCnt, s[1:])
                backtrack(picked + [c], openCnt + 1, closeCnt, s[1:])
            elif c == ")":
                if openCnt > closeCnt:
                    backtrack(picked + [c], openCnt, closeCnt + 1, s[1:])
                backtrack(picked, openCnt, closeCnt, s[1:])
            else:
                backtrack(picked + [c], openCnt, closeCnt, s[1:])
        
        backtrack([], 0, 0, s)
        return self.validSet
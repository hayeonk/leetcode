class Solution(object):
    def scoreOfParentheses(self, S):
        openCnt = closeCnt = 0
        
        ans = i = 0
        for j in xrange(len(S)):
            if S[j] == "(":
                openCnt += 1
            else:
                closeCnt += 1
                
                if openCnt == closeCnt:
                    if openCnt == 1:
                        ans += 1
                    else:
                        ans += 2 * self.scoreOfParentheses(S[i+1:j])
                    i = j + 1
                    openCnt = closeCnt = 0
        return ans
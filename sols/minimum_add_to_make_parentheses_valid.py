class Solution(object):
    def minAddToMakeValid(self, S):
        cnt = left = 0
        for i in xrange(len(S)):
            if S[i] == "(":
                left += 1
            elif left:
                left -= 1
            else:
                cnt += 1
        return cnt + left
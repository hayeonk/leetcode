class Solution(object):
    def generateParenthesis(self, n):
        ret = []
        
        def backtrack(s, l, r):
            if len(s) == 2 * n:
                ret.append(s)
                return
            
            if l == r:
                backtrack(s + "(", l-1, r)
            else:
                if l > 0:
                    backtrack(s + "(", l-1, r)
                backtrack(s + ")", l, r-1)
            
        backtrack("", n, n)
        return ret
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        digits = map(int, list(digits))
        n = len(digits)
        ret = []
        
        def backtrack(s, cur):
            if len(s) == n:
                ret.append(s)
                return
            
            for i in xrange(cur+1, n):
                for c in mapping[digits[i]]:
                    backtrack(s + c, i)      
            
        backtrack("", -1)
        return ret
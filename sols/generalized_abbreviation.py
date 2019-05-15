class Solution(object):
    def generateAbbreviations(self, word):
        ans = []
        
        def backtrack(cur, rest):
            if not rest:
                ans.append(cur)
                return
                
            for i in xrange(len(rest)):
                if cur and cur[-1].isdigit():
                    backtrack(cur + rest[:i+1], rest[i+1:])
                elif cur:
                    backtrack(cur + str(i+1), rest[i+1:])
                else:
                    backtrack(cur + rest[:i+1], rest[i+1:])
                    backtrack(cur + str(i+1), rest[i+1:])
                
        backtrack("", word)
        return ans
            
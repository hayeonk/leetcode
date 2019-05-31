class Solution(object):
    def addOperators(self, num, target):
        N = len(num)
        ans = []
        
        def recurse(index, prevOp, curOp, value, string):
            if index == N:
                if value == target and curOp == 0:
                    ans.append("".join(string[1:])) 
                return
            
            curOp = curOp * 10 + int(num[index])
            strOp = str(curOp)
            
            if curOp > 0:
                recurse(index + 1, prevOp, curOp, value, string)
            
            string.extend(["+", strOp])
            recurse(index + 1, curOp, 0, value + curOp, string)
            string.pop()
            string.pop()
            
            if string:
                string.extend(["-", strOp])
                recurse(index + 1, -curOp, 0, value - curOp, string)
                string.pop()
                string.pop()
                
                string.extend(["*", strOp])
                recurse(index + 1, curOp * prevOp, 0, value - prevOp + curOp * prevOp, string)
                string.pop()
                string.pop()
        
        recurse(0, 0, 0, 0, [])
        return ans
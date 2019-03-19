class Solution(object):
    def isValid(self, s):
        if not s :
            return True
        
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                s = stack.pop()
                if s+c == "()" or s+c == "[]" or s+c == "{}":
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True
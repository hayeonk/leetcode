class Solution(object):
    def validateStackSequences(self, pushed, popped):
        if not pushed:
            return True
        
        stack = []
        
        i = 0
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        
        return not stack
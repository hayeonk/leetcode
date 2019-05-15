# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def recoverFromPreorder(self, S):
        if not S:
            return None
        
        numStack = deque()
        dashStack = deque([0])
        num = cnt = 0
        
        for c in S:
            if c.isdigit():
                num = 10 * num + int(c)
                if cnt:
                    dashStack.append(cnt)
                    cnt = 0
            else:
                if num:
                    numStack.append(num)
                    num = 0
                cnt += 1
        numStack.append(num)
        
        stack = [TreeNode(0)]
        while numStack:
            num = numStack.popleft()
            depth = dashStack.popleft() + 1
            while len(stack) > depth:
                stack.pop()
            
            node = stack[-1]
            if node.left:
                node.right = TreeNode(num)
                stack.append(node.right)
            else:
                node.left = TreeNode(num)
                stack.append(node.left)
        
        return stack[0].left
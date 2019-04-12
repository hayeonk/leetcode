"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        
        ans = deque([])
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.appendleft(node.val)
            for ch in node.children:
                stack.append(ch)
                
        return list(ans)
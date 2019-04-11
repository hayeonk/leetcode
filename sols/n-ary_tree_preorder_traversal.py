"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        if not root:
            return []
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            for ch in reversed(node.children):
                stack.append(ch)
        
        return ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return root
        
        ret = deque([])
        stack = []
        while root:
            stack.append(root)
            ret.appendleft(root.val)
            root = root.right
        
        while stack:
            node = stack.pop().left
            while node:
                stack.append(node)
                ret.appendleft(node.val)
                node = node.right
        return ret
                
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter

class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        
        vals = []
        def traverse(root):
            vals.append(root.val)
            
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        
        traverse(root)
        
        f = Counter(vals)
        maxF = max(f.values())
        return [x for x in f if f[x] == maxF]
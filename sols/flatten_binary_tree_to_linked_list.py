# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        if not root:
            return root
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        
        root.left = None
        root.right = left
        
        l = root
        while l.right:
            l = l.right
        l.right = right
        
        return root
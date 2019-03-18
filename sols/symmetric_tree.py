# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        def isMirror(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isMirror(p.right, q.left) and isMirror(p.left, q.right)
        
        return isMirror(root.left, root.right)
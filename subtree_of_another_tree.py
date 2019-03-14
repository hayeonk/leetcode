# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        def matchTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return matchTree(s.left, t.left) and matchTree(s.right, t.right)
        
        if not t:
            return True
        if not s:
            return False
        if s.val == t.val and matchTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
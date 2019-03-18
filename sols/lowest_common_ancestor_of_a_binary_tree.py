# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root == p and root == q:
            return root
        
        x = self.lowestCommonAncestor(root.left, p, q)
        if x and x != p and x != q:
            return x
        y = self.lowestCommonAncestor(root.right, p, q)
        if y and y != p and y != q:
            return y
        
        if x and y:
            return root
        elif root == p or root == q:
            return root
        else:
            return y if not x else x
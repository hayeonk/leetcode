# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        if not root:
            return [None, None]
        
        if root.val <= V:
            l, r = self.splitBST(root.right, V)
            root.right = l
            return [root, r]
        
        else:
            l, r = self.splitBST(root.left, V)
            root.left = r
            return [l, root]
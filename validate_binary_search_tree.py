import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        def checkBST(root, minV, maxV):
            if not root:
                return True
            if root.val <= minV or root.val >= maxV:
                return False
            return checkBST(root.left, minV, root.val) and checkBST(root.right, root.val, maxV)
        return checkBST(root, -sys.maxint, sys.maxint)
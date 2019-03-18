import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        def checkHeight(root):
            if not root:
                return 0
            left = checkHeight(root.left)
            right = checkHeight(root.right)
            if left == -sys.maxint or right == -sys.maxint:
                return -sys.maxint
            
            if abs(left - right) > 1:
                return -sys.maxint
            
            return 1 + max(left, right)
        
        if checkHeight(root) == -sys.maxint:
            return False
        return True
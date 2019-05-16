# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        if not root:
            return True
        
        if root.left and root.left.val != root.val or not self.isUnivalTree(root.left):
                return False
            
        if root.right and root.right.val != root.val or not self.isUnivalTree(root.right):
                return False
            
        return True
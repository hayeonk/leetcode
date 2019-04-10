# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        
        if not root:
            return root
        
        left = getDepth(root.left)
        right = getDepth(root.right)
        
        if left > right:
            return self.subtreeWithAllDeepest(root.left)
        elif left < right:
            return self.subtreeWithAllDeepest(root.right)
        else:
            return root
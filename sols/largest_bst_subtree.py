# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        if not root:
            return 0
        
        self.ans = 0
        def getLargest(root, minVal, maxVal):
            if not root:
                return True, 0
            
            if root.val <= minVal or root.val >= maxVal:
                return False, 0
            
            lbst, lsize = getLargest(root.left, minVal, root.val)
            rbst, rsize = getLargest(root.right, root.val, maxVal)
            
            if lbst and rbst:
                self.ans = max(self.ans, lsize + rsize + 1)
                return True, lsize + rsize + 1
            
            getLargest(root.left, minVal, maxVal)
            getLargest(root.right, minVal, maxVal)
            
            return False, 0
            
            
        getLargest(root, -float('inf'), float('inf'))
        return self.ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxVal = -987654321
        
    def maxPathSum(self, root):
        def maxPathDown(root):
            if not root:
                return 0
            
            left = max(0, maxPathDown(root.left))
            right = max(0, maxPathDown(root.right))
            self.maxVal = max(self.maxVal, left + right + root.val)
            return max(left, right) + root.val
        
        maxPathDown(root)
        return self.maxVal
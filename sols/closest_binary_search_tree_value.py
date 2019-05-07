# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        self.ans = float('inf')
        
        def traverse(root, target):
            if not root:
                return
            
            if abs(self.ans - target) > abs(root.val - target):
                self.ans = root.val
            
            if root.val > target:
                traverse(root.left, target)
            else:
                traverse(root.right, target)
                
        traverse(root, target)
        
        return self.ans
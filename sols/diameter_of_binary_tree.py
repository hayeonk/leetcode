# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        
        def length(root):
            if not root:
                return 0
            left = length(root.left)
            right = length(root.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        
        length(root)
        return self.ans
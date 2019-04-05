# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        
        height = 0
        left = root
        right = root
        
        while right:
            left = left.left
            right = right.right
            height += 1
        
        if left is None:
            return (1 << height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
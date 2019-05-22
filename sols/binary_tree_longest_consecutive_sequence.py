# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        self.ans = 0
        
        def getLongest(node, parVal, length):
            if not node:
                return
            
            length = length + 1 if parVal is None or parVal + 1 == node.val else 1
            
            self.ans = max(self.ans, length)
            getLongest(node.left, node.val, length)
            getLongest(node.right, node.val, length)
        
        getLongest(root, None, 0)
        return self.ans
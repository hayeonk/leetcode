# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        
        self.ans = 0
        def getLongest(root):
            if not root:
                return 0
            
            left = getLongest(root.left)
            right = getLongest(root.right)
            
            length = ret = 0
            if root.left and root.left.val == root.val:
                length += left + 1
                ret = left + 1
            if root.right and root.right.val == root.val:
                length += right + 1
                ret = max(ret, right + 1)
            
            self.ans = max(self.ans, length)
            return ret
    
        getLongest(root)
        return self.ans
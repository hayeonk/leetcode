# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        self.ans = 0
        
        def traverse(root):
            if not root:
                return
            
            if L <= root.val <= R:
                self.ans += root.val
            
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return self.ans
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        leaf1 = []
        leaf2 = []
        
        def traverse(root, l):
            if not root:
                return
            
            if not root.left and not root.right:
                l.append(root.val)
                return
            
            traverse(root.left, l)
            traverse(root.right, l)
            
        traverse(root1, leaf1)
        traverse(root2, leaf2)
        
        return leaf1 == leaf2
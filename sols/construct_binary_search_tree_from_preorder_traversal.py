# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        left = [x for x in preorder if x < root.val]
        right = [x for x in preorder if x > root.val]
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root
        
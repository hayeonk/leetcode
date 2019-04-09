# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        root = TreeNode(postorder[-1])
        idx = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        
        return root
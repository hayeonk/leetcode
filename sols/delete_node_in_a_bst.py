# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        def findMin(root):
            while root.left:
                root = root.left
            return root.val
        
        def deleteMin(root):
            if not root.left:
                return root.right
            root.left = deleteMin(root.left)
            return root
            
        if not root:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left and root.right:
                root.val = findMin(root.right)
                root.right = deleteMin(root.right)
            elif not root.left:
                return root.right
            else:
                return root.left
        return root
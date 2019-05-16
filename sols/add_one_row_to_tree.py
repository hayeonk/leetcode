# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        def addOneRowDir(root, v, d, left):
            if d == 1:
                new_root = TreeNode(v)
                if left:
                    new_root.left = root
                else:
                    new_root.right = root
                return new_root
            else:
                if not root:
                    return
                root.left = addOneRowDir(root.left, v, d-1, True)
                root.right = addOneRowDir(root.right, v, d-1, False)
                return root
            
        root = addOneRowDir(root, v, d, True)
        return root
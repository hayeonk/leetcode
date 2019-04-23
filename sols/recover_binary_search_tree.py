# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = TreeNode(-987654321)
        
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            if self.prev.val >= root.val:
                if self.first is None:
                    self.first = self.prev
                self.second = root
            self.prev = root
            traverse(root.right)
        
        traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
        return root
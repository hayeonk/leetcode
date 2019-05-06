# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        if not root:
            return 0
        
        self.ans = 0
        
        def isUnivalTree(root):
            if not root.left and not root.right:
                self.ans += 1
                return True
            elif not root.right:
                if isUnivalTree(root.left) and root.left.val == root.val:
                    self.ans += 1
                    return True
                return False
            elif not root.left:
                if isUnivalTree(root.right) and root.right.val == root.val:
                    self.ans += 1
                    return True
                return False
            else:
                left = isUnivalTree(root.left) 
                right = isUnivalTree(root.right)
                if left and right and root.left.val == root.right.val == root.val:
                    self.ans += 1
                    return True
                return False
                
        isUnivalTree(root)
        return self.ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.m = {}
    
    def rob(self, root):
        if not root:
            return 0
        
        if root in self.m:
            return self.m[root]
        
        ans = root.val
        if root.left:
            ans += self.rob(root.left.left) + self.rob(root.left.right)
            
        if root.right:
            ans += self.rob(root.right.left) + self.rob(root.right.right)
        
        ans = max(ans, self.rob(root.left) + self.rob(root.right))
        self.m[root] = ans
        return ans
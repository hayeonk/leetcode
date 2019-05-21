# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        self.ans = 0
        
        def dfs(root):
            children = [0, 0, 0]
            
            if root.left:
                children[dfs(root.left)] += 1
            if root.right:
                children[dfs(root.right)] += 1
            
            if children[0]:
                self.ans += 1
                return 2
            
            if children[2]:
                return 1
            return 0
        
        if not root:
            return 0
        
        if dfs(root) == 0:
            self.ans += 1
        return self.ans
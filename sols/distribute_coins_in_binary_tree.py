# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += abs(left) + abs(right)
            return node.val + left + right - 1
        
        dfs(root)
        return self.ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        
        ans = []
        def traversal(root, level):
            if len(ans) <= level:
                ans.append([])
            
            ans[level].append(root.val)
            
            if root.left:
                traversal(root.left, level + 1)
            if root.right:
                traversal(root.right, level + 1)
        
        traversal(root, 0)
        ans.reverse()
        return ans
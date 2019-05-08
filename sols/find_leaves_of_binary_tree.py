# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        ans = []
        
        def traverse(root):
            if not root:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)
            
            idx = max(left, right)
            if idx >= len(ans):
                ans.append([])
            
            ans[idx].append(root.val)
            return idx + 1
            
        traverse(root)
        return ans
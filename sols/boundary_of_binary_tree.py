# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
        
        ans = [root.val]
        def dfs(root, isLeftBoundary, isRightBoundary):
            if not root:
                return
            
            if isLeftBoundary:
                ans.append(root.val)
                if root.left:
                    dfs(root.left, True, False)
                    dfs(root.right, False, False)
                else:
                    dfs(root.right, True, False)
            
            if not root.left and not root.right:
                if not isLeftBoundary and not isRightBoundary:
                    ans.append(root.val)
                    
            if isRightBoundary:
                if root.right:
                    dfs(root.left, False, False)
                    dfs(root.right, False, True)
                    
                else:
                    dfs(root.left, False, True)
                ans.append(root.val)
            
            if not isLeftBoundary and not isRightBoundary:
                dfs(root.left, False, False)
                dfs(root.right, False, False)
                    
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        
        return ans
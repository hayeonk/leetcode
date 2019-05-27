# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        if N == 1:
            return [TreeNode(0)]
        
        if N == 2:
            return []
        
        ans = []
        for i in xrange(1, N-1):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N - i - 1)
            
            if not left or not right:
                continue
            
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans
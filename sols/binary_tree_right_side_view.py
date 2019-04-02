# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def rightSideView(self, root):
        def rightSide(root, level):
            if not root:
                return
            if len(self.ans) <= level:
                self.ans += [root.val]
            rightSide(root.right, level + 1)
            rightSide(root.left, level + 1)
        
        rightSide(root, 0)
        return self.ans
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        def toString(t):
            if not t:
                return "()"

            left = toString(t.left)
            right = toString(t.right)

            if right == "()":
                right = ""

            if not right and left == "()":
                left = ""

            return "(%d%s%s)" % (t.val, left, right)
        
        return toString(t)[1:-1]
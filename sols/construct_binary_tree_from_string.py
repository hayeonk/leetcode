# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        if not s:
            return None
        
        if "(" not in s:
            return TreeNode(int(s))
        
        i = s.index("(")
        bal = 0
        for j, c in enumerate(s):
            if c == "(": 
                bal += 1
            elif c == ")": 
                bal -= 1
            if i < j and bal == 0:
                break
        
        root = TreeNode(int(s[:i]))
        root.left = self.str2tree(s[i+1:j])
        root.right = self.str2tree(s[j+2:-1])
        
        return root
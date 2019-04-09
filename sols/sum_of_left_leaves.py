# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        ret = 0
        stack = [root]
        
        while stack:
            tmp = stack.pop()
            node = tmp
            while node.left:
                if node.right:
                    stack.append(node.right)
                node = node.left
            if not node.right and node != tmp:
                ret += node.val
            if node.right:
                stack.append(node.right)
        return ret
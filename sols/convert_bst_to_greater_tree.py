# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        total = 0
        
        node = root
        stack = []
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            total += node.val
            node.val = total
            
            node = node.left
        
        return root
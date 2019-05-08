# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        
        stack = [root]
        node = root.left
        while node:
            stack.append(node)
            node = node.left
        
        while stack:
            node = stack.pop()
            
            tmp = node.right
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            
            if node == p:
                if not stack:
                    return None
                return stack.pop()
        return None
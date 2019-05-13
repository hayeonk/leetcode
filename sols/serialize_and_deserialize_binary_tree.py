# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        preorder = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                preorder.append("None")
            else:
                preorder.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return " ".join(preorder)

    def deserialize(self, data):
        preorder = data.split()
        if preorder[0] == "None":
            return None
        
        def traverse(idx):
            if idx >= len(preorder) or preorder[idx] == "None":
                return None, idx + 1
            
            return TreeNode(int(preorder[idx])), idx + 1
            
        root = traverse(0)[0]
        q = deque([root])
        idx = 1
        while idx < len(preorder):
            node = q.popleft()
            if not node:
                continue
            node.left, idx = traverse(idx)
            node.right, idx = traverse(idx)
            q.append(node.left)
            q.append(node.right)
        return root
            
            
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        return str(root.val) + " " + self.serialize(root.left) + " " + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = map(int, data.split())
        root = TreeNode(data[0])
        i = 1
        for i in xrange(1, len(data)+1):
            if i == len(data) or data[i] > root.val:
                break
        root.left = self.deserialize(" ".join(map(str, data[1:i])))
        root.right = self.deserialize(" ".join(map(str, data[i:])))
        return root
    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
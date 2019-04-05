# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        if not root:
            return
        
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        ret = self.stack.pop()
        node = ret.right
        while node:
            self.stack.append(node)
            node = node.left
        
        return ret.val
        

    def hasNext(self):
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
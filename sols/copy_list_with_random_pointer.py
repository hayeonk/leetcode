"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        d = {}
        node = head
        prev = None
        while node:
            newNode = Node(node.val, None, None)
            if prev:
                d[prev].next = newNode
            
            d[node] = newNode
            prev = node
            node = node.next
        
        node = head
        while node:
            newNode = d[node]
            if node.random:
                newNode.random = d[node.random]
            node = node.next
        
        return d[head]
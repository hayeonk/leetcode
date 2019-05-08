"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        node = head
        check = False
        while node.next != head:
            if node.val <= insertVal <= node.next.val or (node.val > node.next.val and insertVal <= node.next.val) or (node.val > node.next.val and insertVal >= node.val):
                newNode = Node(insertVal)
                newNode.next = node.next
                node.next = newNode
                check = True
                break
            
            node = node.next
            
        if not check:
            newNode = Node(insertVal)
            newNode.next = node.next
            node.next = newNode

        return head
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        def flat(head):
            if not head:
                return None, None
            
            node = head
            while node:
                prev = node
                if node.child:
                    chHead, chTail = flat(node.child)
                    node.child = None
                    chHead.prev = node
                    chTail.next = node.next
                    if node.next:
                        node.next.prev = chTail
                    node.next = chHead
                    node = chTail.next
                    prev = chTail
                else:
                    node = node.next
            return head, prev
        
        return flat(head)[0]
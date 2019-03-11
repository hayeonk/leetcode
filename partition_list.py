# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        if head == None:
            return None
        
        beforeStart = beforeEnd = afterStart = afterEnd = None
        node = head
        
        while node != None:
            nextNode = node.next
            if node.val < x:
                if not beforeStart:
                    beforeStart = node
                    beforeEnd = node
                else:
                    beforeEnd.next = node
                    beforeEnd = node
            else:
                if not afterStart:
                    afterStart = node
                    afterEnd = node
                else:
                    afterEnd.next = node
                    afterEnd = node
            node.next = None
            node = nextNode
        
        if beforeStart == None:
            return afterStart
        
        beforeEnd.next = afterStart
        return beforeStart
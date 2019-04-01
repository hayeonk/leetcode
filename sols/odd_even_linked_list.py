# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        
        a = head
        b = head.next
        
        while a.next and b.next:
            a.next = a.next.next
            b.next = b.next.next
            a = a.next
            b = b.next
        
        a.next = even
        return odd
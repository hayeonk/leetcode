# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        rest = self.swapPairs(head.next.next)
        newhead = head.next
        newhead.next = head
        head.next = rest
        return newhead
        
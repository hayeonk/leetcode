# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        cur = head
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
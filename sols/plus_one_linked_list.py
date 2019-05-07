# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        def plus(head):
            if not head.next or plus(head.next):
                if head.val == 9:
                    head.val = 0
                    return True
                else:
                    head.val += 1
                    return False
            
        if plus(head):
            newHead = ListNode(1)
            newHead.next = head
            return newHead
        return head
            
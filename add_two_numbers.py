# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def add(l1, l2, carry):
            if l1 == None and l2 == None and carry == 0:
                return None
            val = carry
            if l1: val += l1.val
            if l2: val += l2.val
            result = ListNode(val % 10)
            
            if l1 or l2:
                if l1: l1 = l1.next
                if l2: l2 = l2.next
                val = 1 if val >= 10 else 0
                more = add(l1, l2, val)
                result.next = more
            return result
        return add(l1, l2, 0)